# Stage 1: Build frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm ci || npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx supervisor curl && rm -rf /var/lib/apt/lists/*

# Python deps
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy backend
COPY backend/ /app/backend/

# Copy built frontend (Vite outputs to dist/ — includes public/ files)
COPY --from=frontend-builder /app/dist /app/frontend/dist

# Copy PDF to dist (in case Vite didn't include binary)
COPY frontend/public/cop-one-pager.pdf /app/frontend/dist/cop-one-pager.pdf

# Configs
COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8080

ENV FLASK_ENV=production
ENV FLASK_CONFIG=production

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8080/api/health || exit 1

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
