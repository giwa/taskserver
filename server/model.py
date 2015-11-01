import datetime
import re

from sqlalchemy import (create_engine,
        Column, Integer, String, ForeignKey,
        DateTime, Date, Text, Float, Index)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import class_mapper

def underscore_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

Base = declarative_base()

# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
# connect to mysql db
# echo True is debugging purpose
engine = create_engine('mysql+mysqldb://ken:ken@localhost/gm', echo=True)

class DBMixin:

    @declared_attr
    def __tablename__(cls):
        return underscore_case(cls.__name__)

    __table_args__ = {'mysql_engine': 'InnoDB'}
    __mapper_args__ = {'always_refresh': True}

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class AssociationMixin:

    @declared_attr
    def __tablename__(cls):
        return underscore_case(cls.__name__)

    __table_args__ = {'mysql_engine': 'InnoDB'}
    __mapper_args__ = {'always_refresh': True}

    id = Column(Integer, primary_key=True)


class User(DBMixin, Base):

    src_ip = Column(String(15))
    date = Column(Date)


class Visit(DBMixin, Base):

    user_id = Column(Integer, ForeignKey("user.id"))
    web_id = Column(Integer, ForeignKey("web.id"))
    # kind represent type of visit to distinguish main or sub
    kind = Column(String(128), index=True)
    stay = Column(Float)
    timestamp = Column(DateTime)

Index('user_web_idx', Visit.web_id, Visit.user_id, unique=True)


class Web(DBMixin, Base):

    task_id = Column(Integer, ForeignKey("task.id"))
    url = Column(Text)
    hashed_url = Column(String(32), index=True)
    http_status = Column(Integer)
    title = Column(Text)
    host = Column(String(512))
    files = relationship("File", backref="web")
    content_type = Column(String(128), index=True)
    content_length = Column(Integer)
    kind = Column(String(128), index=True)


class File(DBMixin, Base):

    web_id = Column(Integer, ForeignKey("web.id"))
    task_id = Column(Integer, ForeignKey("task.id"))
    name = Column(String(1024))
    uri = Column(Text)
    kind = Column(String(128), index=True)


class Task(DBMixin, Base):

    webs = relationship('Web', backref='task')
    files = relationship('File', backref='task')
    name = Column(String(1024))
    kind = Column(String(128), index=True)

    description = Column(Text)
