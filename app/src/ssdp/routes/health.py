from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "ssdp"
    }), 200


@health_bp.get("/ready")
def ready():
    return jsonify({
        "status": "ready"
    }), 200