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

class Timeslot(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    # day = models.ForeignKey(Day, on_delete = modeks.CASCADE)
    slot = models.CharField(max_length = 2)
    status = models.CharField(max_length = 20, default = "empty")
    user = models.CharField(max_length = 100, default = 'none')
    def __str__(self):
        return self.slot
