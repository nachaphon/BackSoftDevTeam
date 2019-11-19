from django.urls import path
from app_mrbs import views

urlpatterns = [
    path('',views.index),
]
