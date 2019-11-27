from django.urls import path
from app_mrbs import views

app_nname = 'mrbs'

urlpatterns = [
    path('',views.HomePageView.as_view()),
    path('user/',views.check_account),
    path('user/pick_day',views.pick_day, name = "pick_day"),
]
