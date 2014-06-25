from django.db.models import Model
from django.db.models.fields import CharField, URLField, BooleanField
from django.db.models.fields.files import ImageField
from django.core.files.storage import FileSystemStorage

class Slide(Model):
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    url = URLField(blank=True)
    image = ImageField(storage=FileSystemStorage('/edx/app/edxapp/uploads/carousel/slides', '/static/uploads/'))
    active = BooleanField()