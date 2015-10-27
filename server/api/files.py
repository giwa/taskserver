from flask import Blueprint, request, abort

from server import di
from server.util import mjsonify

cxt = di.cxt
file_bp = Blueprint('file_api', __name__)


@file_bp.route("", ['GET'])
def list_files():
    files = cxt.dao.file.get_list()
    rs = cxt.scheme.files.dump(files).data
    return mjsonify(rs)


@file_bp.route("/<int:id>", ["GET"])
def get_file(id):
    file = cxt.dao.file.get_by_id(id)
    if not file:
        abort(404)
    rs = cxt.scheme.file.dump(file).data
    return mjsonify(rs)


@file_bp.route("", ["POST"])
def create_file():
    r = request.get_json(force=True)
    if not r:
        abort(400)
    task = cxt.dao.task.get_by_id(r['task_id'])
    web = cxt.dao.task.get_by_id(r['web_id'])
    file = cxt.file.create_with_task_web(
        r.get("name", None),
        r.get("uri", None),
        r.get("kind", None),
        task,
        web
    )
    rs = cxt.scheme.file.dump(file).data
    return mjsonify(rs), 201