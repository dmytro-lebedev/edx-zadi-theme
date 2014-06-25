from django.conf import settings
from django.conf.urls.static import static
from lms import lms

THEME_ROOT = settings.ENV_ROOT / 'themes' / settings.THEME_NAME
settings.MEDIA_ROOT = THEME_ROOT / 'uploads'
settings.MEDIA_URL = '/uploads/'
lms.urls.urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)