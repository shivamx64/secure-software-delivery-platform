from flask import Blueprint, jsonify, request

users_bp = Blueprint("users", __name__)

# in-memory store (temporary)
USERS = [
    {"id": 1, "name": "admin"}
]


@users_bp.get("/users")
def get_users():
    return jsonify(USERS), 200


@users_bp.post("/users")
def create_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400

    new_user = {
        "id": len(USERS) + 1,
        "name": data["name"]
    }

    USERS.append(new_user)

    return jsonify(new_user), 201