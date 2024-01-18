from flask import request, Blueprint

import controllers

users = Blueprint("users", __name__)


@users.route("/user", methods=["POST"])
def user_add():
    return controllers.user_add(request)


@users.route("/users", methods=["GET"])
def users_get_all():
    return controllers.users_get_all()
