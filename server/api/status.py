from flask import Blueprint, request, abort

from server.util import mjsonify

status_bp = Blueprint('status_api', __name__)

@status_bp.route("", methods=["GET"])
def get_status():
    d = dict(status='up')
    return mjsonify(d)
