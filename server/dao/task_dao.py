from server.model import Task
from server.dao.concerns.get_op import GetOp

class TaskDao(GetOp):

    def __init__(self, session):
        self._s = session
        self._m = Task

    def create(self, name, description):
        task = Task(name=name, description=description)
        self._s.add(task)
        return task
