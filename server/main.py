from server.context import Context
from server import di

di.cxt = Context()

from server.api import task_bp, file_bp, web_bp, user_bp, visit_bp, status_bp

app = di.cxt.app
app.register_blueprint(task_bp, url_prefix='/tasks')
app.register_blueprint(file_bp, url_prefix='/files')
app.register_blueprint(web_bp, url_prefix='/webs')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(visit_bp, url_prefix='/visits')
app.register_blueprint(status_bp, url_prefix='/status')
