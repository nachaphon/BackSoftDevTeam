from django.contrib import admin
from app_mrbs import models
# Register your models here.

admin.site.register(models.Account)
admin.site.register(models.Day)
admin.site.register(models.Room)
admin.site.register(models.RoomDay)
admin.site.register(models.Timeslot)
