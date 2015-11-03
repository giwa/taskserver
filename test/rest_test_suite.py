import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker

from server.main import app
from server import model
from server import di


class RestTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        model.engine = create_engine('sqlite:///:memory:')
        model.Base.metadata.create_all(model.engine)
        Session = sessionmaker(bind=model.engine, autocommit=True)
        session = Session()
        di.cxt._session = session
        di.cxt._init_daos()
        #: :type: flask.testing.FlaskClient
        cls.app = app.test_client()
        cls.faker = Faker()

        # Prepare data for test
        cls.task = di.cxt.dao.task.create(name="name", kind="kind", description="desc")
        cls.web = di.cxt.dao.web.create_with_task(
            url="http://foo.baz/example",
            http_status=200,
            title="bar",
            host="foo.baz",
            kind="kind",
            task=cls.task
        )
        cls.file = di.cxt.dao.file.create_with_task_web(
            name="file",
            kind="file_kind",
            uri="/task1/foobarbaz",
            task=cls.task,
            web=cls.web
        )
