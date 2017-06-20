from wtforms import Form, StringField, TextAreaField, validators, DateField
from wtforms import HiddenField, PasswordField

strip_filter = lambda x: x.strip() if x else None


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=255)],
                           filters=[strip_filter])
    password = PasswordField('Password', [validators.Length(min=3)])


class EventCreateForm(Form):
    name = StringField('Team Name', [validators.Length(min=1, max=255)],
                           filters=[strip_filter])
    date = DateField('date')


class EventUpdateForm(EventCreateForm):
    id = HiddenField()
