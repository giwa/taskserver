from server.model import User
from server.dao.concerns.get_op import GetOp

class UserDao(GetOp):

    def __init__(self, cxt):
        self._s = cxt._session
        self._m = User

    def get_by_src_ip(self, src_ip):
        user = self._s.query(User).filter_by(src_ip=src_ip)
        return user

    def get_by_date(self, date):
        users = self._s.query(User).filter_by(date=date)
        return users
