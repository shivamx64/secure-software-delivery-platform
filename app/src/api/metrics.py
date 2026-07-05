"""
User API endpoints.
"""

from flask import Blueprint
from flask import jsonify
from flask import request

from database.db import db
from models import User

users_bp = Blueprint(
    "users",
    __name__,
)


@users_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.order_by(User.id).all()

    return jsonify(
        [user.to_dict() for user in users]
    )


@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)

    return jsonify(user.to_dict())


@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify(
            {
                "error": "Request body is required."
            }
        ), 400

    username = data.get("username")
    email = data.get("email")

    if not username or not email:
        return jsonify(
            {
                "error": "username and email are required."
            }
        ), 400

    user = User(
        username=username,
        email=email,
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "User deleted."
            }
        ),
        200,
    )