from django.db import models
import os
import uuid


# Create your models here.
def upload(instance, filename):
    # ext = filename.split('.')[-1]
    filename = str(uuid.uuid4())
    return os.path.join('pictures', filename)


class Profile(models.Model):
    picture = models.ImageField(upload_to=upload)
