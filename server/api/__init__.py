from server.api.tasks import task_bp
from server.api.files import file_bp
from server.api.users import user_bp
from server.api.visits import visit_bp
from server.api.webs import web_bp
from server.api.status import status_bp


__all__ = [task_bp, file_bp, user_bp, visit_bp, web_bp, status_bp]
