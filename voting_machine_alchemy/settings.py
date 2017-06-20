SOCIAL_AUTH_USER_MODEL = 'example.models.User'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/done'
SOCIAL_AUTH_LOGIN_FUNCTION = 'example.auth.login_user'
SOCIAL_AUTH_LOGGEDIN_FUNCTION = 'example.auth.login_required'

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GooglePlusAuth',
    'social_core.backends.google_openidconnect.GoogleOpenIdConnect',
    'social_core.backends.twitter.TwitterOAuth',
)

SOCIAL_AUTH_TRAILING_SLASH = True

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'common.pipeline.require_email',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.debug.debug',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.debug.debug'
)
