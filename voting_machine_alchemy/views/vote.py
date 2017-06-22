from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from ..forms import VoteForm
from ..models.voting import Event
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
            'vote_form': vote_form}

@view_config(route_name='register-vote', renderer='json')
def register_vote(request):
    return {'success': True}
