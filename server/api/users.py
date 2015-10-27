from flask import Blueprint, request, abort

from server import di
from server.util import mjsonify

cxt = di.cxt
user_bp = Blueprint('user_api', __name__)


@user_bp.route("", ["GET"])
def get_users():
    users = cxt.dao.user.get_list()
    rs = cxt.scheme.users.dump(users).data
    return mjsonify(rs)


@user_bp.route("/<int:id>", ["GET"])
def get_user(id):
    user = cxt.dao.user.get_by_id(id)
    rs = cxt.scheme.user.dump(user).data
    return mjsonify(rs)

