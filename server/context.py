from collections import namedtuple
from sqlalchemy.orm import sessionmaker
from flask import Flask


from server.model import engine
from server.dao import FileDao, TaskDao, UserDao, VisitDao, WebDao
from server.schema import TaskSchema, WebSchema, FileSchema, UserSchema, VisitSchema

Dao = namedtuple("Dao", "file task user visit web")
Schema = namedtuple("Schema", "task tasks web webs file files user users visit visits")

class Context:
    def __init__(self):
        self.app = Flask(__name__)
        Session = sessionmaker(bind=engine)
        self._session = Session()
        self.dao = None
        self.scheme = None
        self._init_daos()
        self._init_schemas()

    def _init_daos(self):
        self.dao = Dao(
            FileDao(self._session),
            TaskDao(self._session),
            UserDao(self._session),
            VisitDao(self._session),
            WebDao(self._session)
        )

    def _init_schemas(self):
        self.scheme = Schema(
            TaskSchema(),
            TaskSchema(many=True),
            WebSchema(),
            WebSchema(many=True),
            FileSchema(),
            FileSchema(many=True),
            UserSchema(),
            UserSchema(many=True),
            VisitSchema(),
            VisitSchema(many=True)
        )

