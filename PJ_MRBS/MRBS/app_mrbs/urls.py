from django.urls import path
from app_mrbs import views

app_nname = 'mrbs'

urlpatterns = [
    path('',views.HomePageView.as_view()),
    path('user/',views.check_account),
]
