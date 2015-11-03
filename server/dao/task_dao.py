from server.model import Task
from server.dao.concerns.get_op import GetOp
from server.dao.sa_dao import SADao

class TaskDao(SADao, GetOp):

    def __init__(self, cxt):
        self._s = cxt._session
        self._m = Task

    def create(self, name, description):
        task = Task(name=name, description=description)
        self._refresh(task)
        return task
