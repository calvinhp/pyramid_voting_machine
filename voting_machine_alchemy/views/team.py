from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from voting_machine_alchemy.services.user import UserService
from ..models.voting import Team
from ..services.team import TeamService
from ..forms import TeamCreateForm, TeamUpdateForm


@view_config(route_name='team_action', match_param='action=create',
             renderer='voting_machine_alchemy:templates/edit_team.jinja2')
def team_create(request):
    event_id = request.matchdict.get('event_id')
    entry = Team(event_id=event_id)
    form = TeamCreateForm(request.POST, entry)
    form.members.query = UserService.all(request)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        request.dbsession.add(entry)
        return HTTPFound(location=request.route_url('event', id=event_id))
    return {'form': form,
            'action': request.matchdict.get('action'),
            'event_id': event_id,
            }


@view_config(route_name='team_action', match_param='action=edit',
             renderer='voting_machine_alchemy:templates/edit_team.jinja2')
def team_update(request):
    team_id = int(request.params.get('id', -1))
    event_id = request.matchdict.get('event_id')
    entry = TeamService.by_id(team_id, request)
    if not entry:
        return HTTPNotFound()
    form = TeamUpdateForm(request.POST, entry)
    form.members.query = UserService.all(request)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        return HTTPFound(
            location=request.route_url('event', id=event_id))
    return {
        'form': form,
        'action': request.matchdict.get('action'),
        'event_id': entry.event_id,
    }
