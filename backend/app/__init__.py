"""
Community of Practice — Flask Backend
======================================
Minimal backend: demo auth + health check. No database.
"""

import os
import time
import hmac
import hashlib
import json
import base64
from flask import Flask, request, jsonify, make_response, session
from flask_cors import CORS


DEMO_SECRET = os.getenv(
    "DEMO_SECRET", "1lIVqJLsOD3nT_1mSWbJ9zFjH3gBrAoPwqpjVGsGbFQ"
)


# ─── Token helpers ───

def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _b64url_decode(s: str) -> bytes:
    padding = 4 - len(s) % 4
    return base64.urlsafe_b64decode(s + "=" * padding)


def verify_demo_token(token):
    """Verify token signature and expiry. Returns payload dict or None."""
    try:
        payload_b64, signature = token.rsplit(".", 1)
    except (ValueError, AttributeError):
        return None

    expected_sig = hmac.new(
        DEMO_SECRET.encode(), payload_b64.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, expected_sig):
        return None

    try:
        payload = json.loads(_b64url_decode(payload_b64))
    except (json.JSONDecodeError, Exception):
        return None

    if time.time() > payload.get("exp", 0):
        return None

    return payload


# ─── App Factory ───

def create_app(config_name=None):
    app = Flask(__name__)

    # Load config
    from .config import config
    cfg = config_name or os.environ.get("FLASK_CONFIG", "development")
    app.config.from_object(config[cfg])

    # CORS for local dev (React on port 5173/6xxx)
    CORS(app, supports_credentials=True, origins=["http://localhost:*", "http://127.0.0.1:*"])

    # ─── Routes ───

    @app.route("/api/health")
    def health():
        return jsonify({"status": "ok"})

    @app.route("/api/demo-auth", methods=["POST"])
    def demo_auth():
        """Validate a demo token and set a session cookie."""
        data = request.get_json(silent=True) or {}
        token = data.get("token", "").strip()

        if not token:
            return jsonify({"error": "Token required"}), 400

        payload = verify_demo_token(token)
        if payload is None:
            return jsonify({"error": "Invalid or expired token"}), 401

        # Store in Flask session
        session["demo_authenticated"] = True
        session["demo_event"] = payload.get("event", "Demo")
        session["demo_exp"] = payload.get("exp", 0)

        response = make_response(jsonify({
            "authenticated": True,
            "event": payload.get("event", "Demo"),
        }))
        return response

    @app.route("/api/demo-status")
    def demo_status():
        """Check whether the current session is authenticated."""
        if session.get("demo_authenticated"):
            exp = session.get("demo_exp", 0)
            if time.time() < exp:
                return jsonify({
                    "authenticated": True,
                    "event": session.get("demo_event", "Demo"),
                })
            # Expired — clear session
            session.clear()

        return jsonify({"authenticated": False})

    # ─── Demo gate (before_request) ───

    DEMO_AUTH_ENABLED = os.getenv("DEMO_AUTH_ENABLED", "false").lower() == "true"
    PUBLIC_PATHS = {"/api/health", "/api/demo-auth", "/api/demo-status", "/health"}
    PUBLIC_PREFIXES = ("/static/", "/assets/")

    @app.before_request
    def check_demo_auth():
        if not DEMO_AUTH_ENABLED:
            return
        path = request.path
        if path in PUBLIC_PATHS:
            return
        if any(path.startswith(p) for p in PUBLIC_PREFIXES):
            return
        if session.get("demo_authenticated"):
            exp = session.get("demo_exp", 0)
            if time.time() < exp:
                return
            session.clear()
        return jsonify({"error": "Demo authentication required"}), 401

    return app
