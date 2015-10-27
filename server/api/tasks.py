from flask import Blueprint, request, abort

from server import di
from server.util import mjsonify

cxt = di.cxt
task_bp = Blueprint('task_api', __name__)


@task_bp.route("", methods=['GET'])
def list_tasks():
    tasks = cxt.dao.task.get_list()
    r = cxt.scheme.tasks.dump(tasks).data
    return mjsonify(r)


@task_bp.route("/<int:id>", methods=['GET'])
def get_task(id):
    task = cxt.dao.task.get_by_id(id)
    if not task:
        abort(404)
    r = cxt.scheme.task.dump(task).data
    return mjsonify(r)


@task_bp.route("", methods=['POST'])
def create_task():
    r = request.get_json(force=True)
    if not r:
        abort(400)
    task = cxt.dao.task.create(name=r['name'], description=r['description'])
    r = cxt.scheme.task.dump(task).data
    return mjsonify(r), 201
