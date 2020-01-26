from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=50, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)