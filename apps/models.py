from django.db import models
from django.db.models import CASCADE
from django_ckeditor_5.fields import CKEditor5Field


class Friend(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='apps.Friend')
