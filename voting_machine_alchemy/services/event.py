import sqlalchemy as sa
from ..models.voting import Event


class EventService(object):

    @classmethod
    def all(cls, request):
        query = request.dbsession.query(Event)
        return query.order_by(sa.desc(Event.date))

    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(Event)
        return query.get(_id)
