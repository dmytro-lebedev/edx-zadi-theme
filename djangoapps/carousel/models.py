from django.db.models import Model
from django.db.models.fields import CharField, URLField, BooleanField
from django.db.models.fields.files import ImageField
from django.core.files.storage import FileSystemStorage
from .settings import THEME_MEDIA_ROOT, THEME_MEDIA_URL

class Slide(Model):
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    url = URLField(blank=True)
    image = ImageField(storage=FileSystemStorage('{}/carousel/slides/'.format(THEME_MEDIA_ROOT), '{}/carousel/slides/'.format(THEME_MEDIA_URL)))
    active = BooleanField()