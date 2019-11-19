from django.urls import path
from app_mrbs import views

urlpatterns = [
    path('',views.HomePageView.as_view()),
    path('user/',views.check_account),
]
