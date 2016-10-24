import os
import uuid

from django.db import models


def upload(instance, filename):
    filename = str(uuid.uuid4())
    return os.path.join('pictures', filename)


class Profile(models.Model):
    picture = models.ImageField(upload_to=upload)
