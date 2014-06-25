from django.conf import settings

THEME_ROOT = settings.ENV_ROOT / 'themes' / settings.THEME_NAME
THEME_MEDIA_ROOT = THEME_ROOT / 'uploads'
THEME_MEDIA_URL = 'uploads'

settings.STATICFILES_DIRS.append(
    (THEME_MEDIA_URL, THEME_MEDIA_ROOT)
)