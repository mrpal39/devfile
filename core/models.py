from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class platform(models.Model):
    name=CharField(max_length=50)
    project_count=IntegerField()
    homepage=CharField(max_length=50)
    color=CharField(max_length=50)
    # default_language=CharField(max_length=50)

    def __str__(self):
        return self.name
    