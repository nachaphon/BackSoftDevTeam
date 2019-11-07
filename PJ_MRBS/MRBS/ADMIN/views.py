from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def show_admin(request):
    return HttpResponse("<h1>Show Admin<h1>")
