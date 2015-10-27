from flask import jsonify, request, abort

from server.context import Context


cxt = Context()
app = cxt.app


@app.route("/tasks", ['GET'])
def list_tasks():
    tasks = cxt.dao.task.get_list()
    return jsonify(cxt.scheme.tasks(tasks))


@app.route("/tasks/<int:id>", ['GET'])
def get_task(id):
    task = cxt.dao.task.get_by_id(id)
    if not task:
        abort(404)
    return jsonify(cxt.scheme.task(task))


@app.route("/tasks", ['POST'])
def create_task():
    r = request.get_json(force=True)
    if not r:
        abort(400)
    task = cxt.dao.task.create(name=r['name'], description=r['description'])
    return jsonify(cxt.scheme.task(task)), 201


@app.route("/webs", ['GET'])
def list_webs():
    webs = cxt.dao.web.get_list()
    return jsonify(cxt.scheme.webs(webs))


@app.route("/webs/<int:id>", ["GET"])
def get_web(id):
    web = cxt.dao.web.get_by_id(id)
    if not web:
        abort(404)
    return jsonify(cxt.scheme.web(web))


@app.route("/webs", ["POST"])
def create_web():
    r = request.get_json(force=True)
    if not r:
        abort(400)
    task = cxt.dao.task.get_by_id(r['task_id'])
    web = cxt.dao.web.create_with_task_file(
        r.get('url', None),
        r.get('hashed_url', None),
        r.get('http_status', None),
        r.get('title', None),
        r.get('host', None),
        task,
        r.get('files', [])
    )
    return jsonify(cxt.scheme.web(web)), 201


@app.route("/files", ['GET'])
def get_files():
    files = cxt.dao.file.get_list()
    return jsonify(cxt.dao.files(files))


@app.route("/files/<int:id>", ['GET'])
def get_file(id):
    file = cxt.dao.file.get_by_id(id)
    if not file:
        abort(404)
    return jsonify(cxt.scheme.file(file))


@app.route("/files", ["POST"])
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
    return jsonify(cxt.scheme.file(file)), 201


@app.route("/users", ["GET"])
def get_users():
    users = cxt.dao.user.get_list()
    return jsonify(cxt.scheme.users(users))

@app.route("/users/<int:id>", ["GET"])
def get_user(id):
    user = cxt.dao.user.get_by_id(id)
    return jsonify(cxt.scheme.user(user))


