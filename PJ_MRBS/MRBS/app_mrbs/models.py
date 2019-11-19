from django.db import models

# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    def __str__(self):
        return self.user_name