import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_new_user():
        return Users("", "")


class UsersSchema(ma.Schema):
    class Meta:
        fields = ["user_id", "email"]


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
