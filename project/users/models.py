from django.contrib.postgres.fields import ArrayField
from django.db import models

# user -> id(IntegerField), name(CharField), gender(CharField)
# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    rink = models.CharField(max_length=255)
    gender = ArrayField(models.CharField(max_length=20), blank=True)
    color = ArrayField(models.CharField(max_length=20), blank=True)
    part = ArrayField(models.CharField(max_length=20), blank=True)
    tag = ArrayField(models.CharField(max_length=20), blank=True)
    score = models.IntegerField(default=0)
