from django.db import Model
from django.db.models.fields import CharField, URLField, BooleanField
from django.db.models.fields.files import ImageField

class Slide(Model):
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    url = URLField(blank=True)
    image = ImageField(upload_to='carousel/slides')
    active = BooleanField()