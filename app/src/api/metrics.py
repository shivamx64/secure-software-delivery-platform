from flask import Blueprint, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

metric_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/metrics", methods=["GET"])
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT
    )