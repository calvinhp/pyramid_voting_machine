import datetime
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class Event(Base):
    """A specific event requiring voting"""
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date = Column(DateTime, default=datetime.datetime.utcnow)



Index('my_index', Event.name, unique=True, mysql_length=255)


class Team(Base):
    """A grouping of users associated with an Event"""
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)


class Vote(Base):
    """A vote for a team made by a User"""
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
