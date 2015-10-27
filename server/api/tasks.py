from flask import Blueprint, jsonify, request, abort

from server import di

cxt = di.cxt
task_bp = Blueprint('task_api', __name__)


@task_bp.route("/", methods=['GET'])
def list_tasks():
    tasks = cxt.dao.task.get_list()
    return jsonify(cxt.scheme.tasks(tasks))


@task_bp.route("/<int:id>", methods=['GET'])
def get_task(id):
    task = cxt.dao.task.get_by_id(id)
    if not task:
        abort(404)
    return jsonify(cxt.scheme.task(task))


@task_bp.route("/", methods=['POST'])
def create_task():
    r = request.get_json(force=True)
    if not r:
        abort(400)
    task = cxt.dao.task.create(name=r['name'], description=r['description'])
    return jsonify(cxt.scheme.task(task)), 201
