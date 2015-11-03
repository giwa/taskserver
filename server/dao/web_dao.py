from server.model import Web
from server.dao.concerns.get_op import GetOp
from server.dao.sa_dao import SADao
import hashlib


class WebDao(SADao, GetOp):

    def __init__(self, cxt):
        self._s = cxt._session
        self._m = Web

    def create(self, url, http_status, title, host, kind):
        web = Web(url=url, hashed_url=self._hash(url), http_status=http_status, title=title, host=host, kind=kind)
        self._s.add(web)
        self._refresh(web)
        return web

    def create_with_task(self, url, http_status, title, host, kind, task):
        web = Web(url=url, hashed_url=self._hash(url), http_status=http_status, title=title, host=host, kind=kind)
        task.webs.append(web)
        self._refresh(web)
        return web

    def create_with_task_file(self, url, http_status, title, host, kind, task, files):
        web = Web(url=url, hashed_url=self._hash(url), http_status=http_status, title=title, host=host, kind=kind)
        if task:
            task.webs.append(web)
        for f in files:
            web.files.append(f)
        self._refresh(web)
        return web

    def _hash(self, obj):
        return hashlib.md5(obj.encode()).hexdigest()
