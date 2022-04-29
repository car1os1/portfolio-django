from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class project(models.Model):

    title = models.CharField(max_length=100)
    descripction = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)