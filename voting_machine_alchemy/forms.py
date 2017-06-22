from wtforms import Form, StringField, validators, DateField, RadioField
from wtforms import HiddenField, PasswordField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField

strip_filter = lambda x: x.strip() if x else None


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=255)],
                           filters=[strip_filter])
    password = PasswordField('Password', [validators.Length(min=3)])


class EventCreateForm(Form):
    name = StringField('Event Name', [validators.Length(min=1, max=255)],
                           filters=[strip_filter])
    date = DateField('Date')


class EventUpdateForm(EventCreateForm):
    id = HiddenField()


class TeamCreateForm(Form):
    event_id = HiddenField()
    name = StringField('Team Name', [validators.Length(min=1, max=255)],
                       filters=[strip_filter])
    members = QuerySelectMultipleField('Team Members', get_label='name')


class TeamUpdateForm(TeamCreateForm):
    id = HiddenField()


class VoteForm(Form):
    """ Create a set of radio buttons for a category """
    vote_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
    )
    awesomeness = RadioField('Awesomeness', choices=vote_choices)
    completeness = RadioField('Completeness', choices=vote_choices)
    usefulness = RadioField('Usefulness', choices=vote_choices)
