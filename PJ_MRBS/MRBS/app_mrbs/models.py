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
    day = models.ForeignKey(Day, on_delete = models.CASCADE)
    room_name = models.CharField(max_length = 100)
    room_seat = models.CharField(max_length = 3)
    def __str__(self):
        return self.room_name

class Timeslot(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    # day = models.ForeignKey(Day, on_delete = modeks.CASCADE)
    # slot1 = models.CharField(max_length = 2)
    of_room = models.CharField(max_length = 100, default = "NONE")



    status1 = models.CharField(max_length = 20, default = "empty")
    user1 = models.CharField(max_length = 100, default = 'none')

    # slot2 = models.CharField(max_length = 2)
    status2 = models.CharField(max_length = 20, default = "empty")
    user2 = models.CharField(max_length = 100, default = 'none')

    # slot3 = models.CharField(max_length = 2)
    status3 = models.CharField(max_length = 20, default = "empty")
    user3 = models.CharField(max_length = 100, default = 'none')

    # slot4 = models.CharField(max_length = 2)
    status4 = models.CharField(max_length = 20, default = "empty")
    user4 = models.CharField(max_length =  100, default = 'none')

    # slot5 = models.CharField(max_length = 2)
    status5 = models.CharField(max_length = 20, default = "empty")
    user5 = models.CharField(max_length = 100, default = 'none')

    # slot6 = models.CharField(max_length = 2)
    status6 = models.CharField(max_length = 20, default = "empty")
    user6 = models.CharField(max_length = 100, default = 'none')

    # slot7 = models.CharField(max_length = 2)
    status7 = models.CharField(max_length = 20, default = "empty")
    user7 = models.CharField(max_length = 100, default = 'none')

    # slot8 = models.CharField(max_length = 2)
    status8 = models.CharField(max_length = 20, default = "empty")
    user8 = models.CharField(max_length = 100, default = 'none')

    # slot9 = models.CharField(max_length = 2)
    status9 = models.CharField(max_length = 20, default = "empty")
    user9 = models.CharField(max_length = 100, default = 'none')

    # slot10 = models.CharField(max_length = 2)
    status10 = models.CharField(max_length = 20, default = "empty")
    user10 = models.CharField(max_length = 100, default = 'none')

    # slot11 = models.CharField(max_length = 2)
    status11 = models.CharField(max_length = 20, default = "empty")
    user11 = models.CharField(max_length = 100, default = 'none')

    # slot12 = models.CharField(max_length = 2)
    status12 = models.CharField(max_length = 20, default = "empty")
    user12 = models.CharField(max_length = 100, default = 'none')

    # slot13 = models.CharField(max_length = 2)
    status13 = models.CharField(max_length = 20, default = "empty")
    user13 = models.CharField(max_length = 100, default = 'none')

    # slot14 = models.CharField(max_length = 2)
    status14 = models.CharField(max_length = 20, default = "empty")
    user14 = models.CharField(max_length = 100, default = 'none')

    # slot15 = models.CharField(max_length = 2)
    status15 = models.CharField(max_length = 20, default = "empty")
    user15 = models.CharField(max_length = 100, default = 'none')

    # slot16 = models.CharField(max_length = 2)
    status16 = models.CharField(max_length = 20, default = "empty")
    user16 = models.CharField(max_length = 100, default = 'none')
    def __str__(self):
        return self.of_room
