from datetime import datetime

from database.db import db


class Task(db.Model):

    __tablename__ = "tasks"

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Task title
    title = db.Column(
        db.String(255),
        nullable=False,
    )

    # Optional description
    description = db.Column(
        db.Text,
        nullable=True,
    )

    # Task status
    completed = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    # Audit timestamps
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    def __repr__(self) -> str:

        return f"<Task id={self.id} title='{self.title}'>"