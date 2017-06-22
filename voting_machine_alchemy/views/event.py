from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from ..models.voting import Event
from ..services.event import EventService
from ..services.team import TeamService
from ..forms import EventCreateForm, EventUpdateForm


@view_config(route_name='event',
             renderer='voting_machine_alchemy:templates/view_event.jinja2')
def event_view(request):
    event_id = int(request.matchdict.get('id', -1))
    entry = EventService.by_id(event_id, request)
    teams = TeamService.all_by_event(event_id, request)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry,
            'teams': teams}


@view_config(route_name='event_action', match_param='action=create',
             renderer='voting_machine_alchemy:templates/edit_event.jinja2')
def event_create(request):
    entry = Event()
    form = EventCreateForm(request.POST)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        request.dbsession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='event_action', match_param='action=edit',
             renderer='voting_machine_alchemy:templates/edit_event.jinja2')
def event_update(request):
    event_id = int(request.params.get('id', -1))
    entry = EventService.by_id(event_id, request)
    if not entry:
        return HTTPNotFound()
    form = EventUpdateForm(request.POST, entry)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        return HTTPFound(
            location=request.route_url('event', id=entry.id))
    return {'form': form, 'action': request.matchdict.get('action')}
