from server.model import User
from server.dao.concerns.get_op import GetOp

class UserDao(GetOp):

    def __init__(self, session):
        self._s = session
        self._m = User

    def get_by_src_ip(self, src_ip):
        with self._s.begin():
            user = self._s.query(User).filter_by(src_ip=src_ip)
            return user

    def get_by_date(self, date):
        with self._s.begin():
            users = self._s.query(User).filter_by(date=date)
            return users
