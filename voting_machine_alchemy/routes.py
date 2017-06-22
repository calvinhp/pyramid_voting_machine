def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/sign/{action}')
    config.add_route('register', '/register')
    config.add_route('event', '/event/{id}/detail')
    config.add_route('event_action', '/event/{action}')

    config.add_route('team_action', '/event/{event_id}/team/{action}')
