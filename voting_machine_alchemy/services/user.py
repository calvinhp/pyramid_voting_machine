from ..models.user import User


class UserService(object):

    @classmethod
    def all(cls, request):
        return request.dbsession.query(User)

    @classmethod
    def by_name(cls, name, request):
        return request.dbsession.query(User).filter(User.name == name).first()
