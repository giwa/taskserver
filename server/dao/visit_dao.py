from server.model import Visit
from server.dao.concerns.get_op import GetOp

class VisitDao(GetOp):

    def __init__(self, cxt):
        self._s = cxt._session
        self._m = Visit

    def get_by_timestamp(self, lower=None, upper=None):
        pass
