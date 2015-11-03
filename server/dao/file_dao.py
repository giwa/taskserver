from server.model import File
from server.dao.concerns.get_op import GetOp
from server.dao.sa_dao import SADao


class FileDao(SADao, GetOp):

    def __init__(self, cxt):
        self._s = cxt._session
        self._m = File

    def create(self, name, uri, kind):
        file = self.create_with_task_web(name, uri, kind, None, None)
        return file

    def create_with_task(self, name, uri, kind, task):
        file = self.create_with_task_web(name, uri, kind, task, None)
        return file

    def create_with_task_web(self, name, uri, kind, task, web):
        file = File(name=name, uri=uri, kind=kind)
        if task:
            task.files.append(file)
        if web:
            web.files.append(file)
        self._refresh(file)
        return file
