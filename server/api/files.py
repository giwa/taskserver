from flask import Blueprint, request, abort

from server import di
from server.util import mjsonify

cxt = di.cxt
file_bp = Blueprint('file_api', __name__)


@file_bp.route("", methods=['GET'])
def list_files():
    files = cxt.dao.file.get_list()
    rs = cxt.scheme.files.dump(files).data
    return mjsonify(rs)


@file_bp.route("/<int:id>", methods=["GET"])
def get_file(id):
    file = cxt.dao.file.get_by_id(id)
    if not file:
        abort(404)
    rs = cxt.scheme.file.dump(file).data
    return mjsonify(rs)


@file_bp.route("", methods=["POST"])
def create_file():
    r = request.get_json(force=True)
    if not r:
        abort(400)
    task = cxt.dao.task.get_by_id(r['task_id'])
    web = cxt.dao.web.get_by_id(r['web_id'])
    file = cxt.dao.file.create_with_task_web(
        r.get("name", None),
        r.get("uri", None),
        r.get("kind", None),
        task,
        web
    )
    rs = cxt.scheme.file.dump(file).data
    return mjsonify(rs), 201
