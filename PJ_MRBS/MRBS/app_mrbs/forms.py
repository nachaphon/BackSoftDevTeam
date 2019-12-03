from django.forms import ModelForm
from .models import Room, Timeslot, Sortmodel
from django import forms

# class Timeslotform(ModelForm):
#     class Meta:
#         model = Timeslot
#         fields = ['status1', 'status2']
# class Fooform(forms.Form):
#     btn = forms.CharField()

Seat = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20'),
    ('21','21'),
    ('22','22'),
    ('23','23'),
    ('24','24'),
    ('25','25'),
)
Period = (
    ('0.5', '0.5'),
    ('1', '1'),
    ('1.5', '1.5'),
    ('2', '2'),
    ('2.5', '2.5'),
    ('3', '3'),
    ('3.5', '3.5'),
    ('4', '4'),
)

class Sortform(forms.Form):
    seat    = forms.ChoiceField(choices=Seat, required=True )
    period   = forms.ChoiceField(choices=Period , required=True )
