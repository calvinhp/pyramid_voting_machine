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
