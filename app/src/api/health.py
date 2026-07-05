from flask import Blueprint, jsonify

helath_bp = Blueprint(
    "health",
    __name__,
)

@health_bp.route("/health", methods=["GET"])
def health():
    return (
        jsonify(
            {
                "status": "healthty",
            }
        ),
        200,
    )