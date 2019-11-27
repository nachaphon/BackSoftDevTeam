from django.db import models

# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    def __str__(self):
        return self.user_name

class Day(models.Model):
    day = models.CharField(max_length = 2)
    def __str__(self):
        return self.day

class Room(models.Model):
    day = models.ForeignKey(Day, on_delete = models.CASCADE)
    room_name = models.CharField(max_length = 100)
    room_seat = models.CharField(max_length = 3)
    def __str__(self):
        return self.room_name
