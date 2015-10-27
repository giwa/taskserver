from server.context import Context
from server import di

di.cxt = Context()

from server.api import task_bp

app = di.cxt.app
app.register_blueprint(task_bp, url_prefix='/tasks')


