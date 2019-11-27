from django.forms import ModelForm
from .models import Room, Timeslot
from django import forms


class Timeslotform(ModelForm):
    class Meta:
        model = Timeslot
        fields = ['status']
