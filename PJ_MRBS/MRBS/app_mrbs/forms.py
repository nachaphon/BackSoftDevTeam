from django.forms import ModelForm
from .models import Room, Timeslot
from django import forms

class Timeslotform(ModelForm):
    class Meta:
        model = Timeslot
        fields = ['status1', 'status2']
# class Fooform(forms.Form):
#     btn = forms.CharField()
