from django.conf import settings

THEME_ROOT = settings.ENV_ROOT / 'themes' / settings.THEME_NAME
THEME_MEDIA_ROOT = THEME_ROOT / 'static' / 'uploads'
THEME_MEDIA_URL = 'themes/{}/uploads'.format(settings.THEME_NAME)