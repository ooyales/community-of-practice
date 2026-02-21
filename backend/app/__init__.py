"""
Community of Practice — Flask Backend
======================================
Minimal backend: demo auth + health check. No database.
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS


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

    # ─── Shared demo auth (injected by build script for AWS) ───
    try:
        from demo_auth import init_demo_auth
        init_demo_auth(app, session_manager=None)
    except ImportError:
        pass  # Local dev — no demo auth needed

    return app
