from ..models.voting import Team


class TeamService(object):

    @classmethod
    def all_by_event(cls, _event_id, request):
        query = request.dbsession.query(Team)
        return query.filter(Team.event_id == _event_id)

    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(Team)
        return query.get(_id)
