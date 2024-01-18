from flask import jsonify

from db import db
from util.reflection import populate_object
from models.users import Users, user_schema, users_schema


def user_add(req):
    post_data = req.form if req.form else req.json
    new_user = Users.get_new_user()

    populate_object(new_user, post_data)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user)), 201
