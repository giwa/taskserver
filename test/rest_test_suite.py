import unittest
import os
import sys
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SERVER_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
sys.path.append(SERVER_PATH)

from faker import Faker
from server.main import app
from server import model
from server import di

class RestTestSuite(unittest.TestCase):
    def setUp(self):
        model.engine = create_engine('sqlite:///:memory:')
        model.Base.metadata.create_all(model.engine)
        Session = sessionmaker(bind=model.engine, autocommit=True)
        session = Session()
        di.cxt._session = session
        di.cxt._init_daos()
        #: :type: flask.testing.FlaskClient
        self.app = app.test_client()
        self.faker = Faker()
