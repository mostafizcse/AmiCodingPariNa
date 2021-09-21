from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    user_id = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=200)
    input_values = models.CharField(max_length=200)

    def __str__(self):
        return self.current_user



