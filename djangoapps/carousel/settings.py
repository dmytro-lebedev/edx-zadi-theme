from django.conf import settings

MEDIA_ROOT = '/edx/var/edxapp/staticfiles/themes/{}/uploads'.format(settings.THEME_NAME)
MEDIA_URL = '/static/themes/{}/uploads/'.format(settings.THEME_NAME)