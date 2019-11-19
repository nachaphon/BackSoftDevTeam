from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse
from .templates import app_mrbs

# Create your views here.



def index(request):
    return render(request,'app_mrbs/index.html')