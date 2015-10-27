from server.model import Web
from server.dao.concerns.get_op import GetOp

class WebDao(GetOp):

    def __init__(self, session):
        self._s = session
        self._m = Web

    def create(self, url, hashed_url, http_status, title, host):
        web = Web(url=url, hashed_url=hashed_url, http_status=http_status, title=title, host=host)
        self._s.add(web)
        return web

    def create_with_task(self, url, hashed_url, http_status, title, host, task):
        web = Web(url=url, hashed_url=hashed_url, http_status=http_status, title=title, host=host)
        task.webs.append(web)
        return web

    def create_with_task_file(self, url, hashed_url, http_status, title, host, task, files):
        web = Web(url=url, hashed_url=hashed_url, http_status=http_status, title=title, host=host)
        if task:
            task.webs.append(web)
        for f in files:
            web.files.append(f)
        self._s.add(web)
        return web
