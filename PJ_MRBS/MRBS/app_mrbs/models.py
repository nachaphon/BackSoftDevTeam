from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100, default = "user")
    def __str__(self):
        return self.username

class Day(models.Model):
    day = models.CharField(max_length = 2)
    def __str__(self):
        return self.day

class Room(models.Model):
    room_name = models.CharField(max_length = 100)
    room_seat = models.CharField(max_length = 3)
    def __str__(self):
        return self.room_name

class RoomDay(models.Model):
    day = models.ForeignKey(Day, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    def __str__(self):
        return (str(self.day)+"_"+str(self.room))


class Timeslot(models.Model):
    roomday = models.ForeignKey(RoomDay, on_delete = models.CASCADE)

    status1 = models.CharField(max_length = 20, default = "empty")
    user1 = models.CharField(max_length = 100, default = 'none')

    status2 = models.CharField(max_length = 20, default = "empty")
    user2 = models.CharField(max_length = 100, default = 'none')

    status3 = models.CharField(max_length = 20, default = "empty")
    user3 = models.CharField(max_length = 100, default = 'none')

    status4 = models.CharField(max_length = 20, default = "empty")
    user4 = models.CharField(max_length =  100, default = 'none')

    status5 = models.CharField(max_length = 20, default = "empty")
    user5 = models.CharField(max_length = 100, default = 'none')

    status6 = models.CharField(max_length = 20, default = "empty")
    user6 = models.CharField(max_length = 100, default = 'none')

    status7 = models.CharField(max_length = 20, default = "empty")
    user7 = models.CharField(max_length = 100, default = 'none')

    status8 = models.CharField(max_length = 20, default = "empty")
    user8 = models.CharField(max_length = 100, default = 'none')

    status9 = models.CharField(max_length = 20, default = "empty")
    user9 = models.CharField(max_length = 100, default = 'none')

    status10 = models.CharField(max_length = 20, default = "empty")
    user10 = models.CharField(max_length = 100, default = 'none')

    status11 = models.CharField(max_length = 20, default = "empty")
    user11 = models.CharField(max_length = 100, default = 'none')

    status12 = models.CharField(max_length = 20, default = "empty")
    user12 = models.CharField(max_length = 100, default = 'none')

    status13 = models.CharField(max_length = 20, default = "empty")
    user13 = models.CharField(max_length = 100, default = 'none')

    status14 = models.CharField(max_length = 20, default = "empty")
    user14 = models.CharField(max_length = 100, default = 'none')

    status15 = models.CharField(max_length = 20, default = "empty")
    user15 = models.CharField(max_length = 100, default = 'none')

    status16 = models.CharField(max_length = 20, default = "empty")
    user16 = models.CharField(max_length = 100, default = 'none')
    def __str__(self):
        return ("Timeslot of_"+str(self.roomday))
