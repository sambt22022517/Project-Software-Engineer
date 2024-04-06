from typing import Any
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    telephone = models.IntegerField(null=False)
    password = models.CharField(max_length=20)