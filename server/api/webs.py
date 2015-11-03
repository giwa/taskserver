from flask import Blueprint, request, abort

from server import di
from server.util import mjsonify

cxt = di.cxt
web_bp = Blueprint('web_api', __name__)


@web_bp.route("", methods=['GET'])
def list_webs():
    webs = cxt.dao.web.get_list()
    rs = cxt.scheme.webs.dump(webs).data
    return mjsonify(rs)


@web_bp.route("/<int:id>", methods=["GET"])
def get_web(id):
    web = cxt.dao.web.get_by_id(id)
    if not web:
        abort(404)
    rs = cxt.scheme.web.dump(web).data
    return mjsonify(rs)


@web_bp.route("", methods=["POST"])
def create_web():
    r = request.get_json(force=True)
    if not r:
        abort(400)
    task = cxt.dao.task.get_by_id(r['task_id'])
    web = cxt.dao.web.create_with_task(
        r.get('url', None),
        r.get('http_status', None),
        r.get('title', None),
        r.get('host', None),
        r.get('kind', None),
        task
    )
    rs = cxt.scheme.web.dump(web).data
    return mjsonify(rs), 201
