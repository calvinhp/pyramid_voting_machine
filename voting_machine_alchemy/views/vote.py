from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from voting_machine_alchemy.services.user import UserService
from ..forms import VoteForm
from ..models.user import User
from ..models.voting import Event
from ..models.voting import Vote
from ..services.event import EventService
from ..services.team import TeamService


@view_config(route_name='vote',
             renderer='voting_machine_alchemy:templates/view_vote.jinja2')
def vote_view(request):
    event_id = int(request.matchdict.get('id', -1))
    entry = EventService.by_id(event_id, request)
    teams = TeamService.all_by_event(event_id, request)
    vote_form = VoteForm()
    if not entry:
        return HTTPNotFound()
    return {'entry': entry,
            'teams': teams,
            'event_id': event_id,
            'vote_form': vote_form}

@view_config(route_name='register-vote', renderer='json')
def register_vote(request):
    event_id = int(request.matchdict.get('event_id', -1))
    user_id = request.authenticated_userid
    event = EventService.by_id(event_id, request)
    user = UserService.by_name(user_id, request)
    vote = Vote()
    vote.event_id = event_id
    vote.team_id = request.POST.get('team_id')
    vote.category = request.POST.get('category')
    vote.value = request.POST.get('value')
    return {'success': True}
