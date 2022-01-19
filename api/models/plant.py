from django.db import models
from django.contrib.auth import get_user_model

class Plant(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    