import datetime
from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    Table,
)
from sqlalchemy.orm import relationship

from .meta import Base


class Event(Base):
    """A specific event requiring voting"""
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date = Column(DateTime, default=datetime.datetime.utcnow)

team_association_table = Table('team_membership', Base.metadata,
    Column('team_id', Integer, ForeignKey('teams.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class Team(Base):
    """A grouping of users associated with an Event"""
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    event_id = Column(ForeignKey('events.id'), nullable=False)
    name = Column(Text)
    members = relationship('User', secondary=team_association_table)


class Vote(Base):
    """A vote for a team made by a User"""
    __tablename__ = 'votes'
    event_id = Column(ForeignKey('events.id'), nullable=False, primary_key=True)
    team_id = Column(ForeignKey('teams.id'), nullable=False, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, primary_key=True)
    category = Column(String, nullable=False, primary_key=True)
    value = Column(Integer, nullable=False, primary_key=True)
