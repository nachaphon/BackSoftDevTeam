from django.urls import path
from app_mrbs import views

app_name = 'mrbs'

urlpatterns = [
    path('',views.HomePageView.as_view()),
    path('user/',views.check_account),
    path('user/pick_day',views.pick_day, name = "pick_day"),
    path('user/pick_day/pick_room/<int:day_id>',views.pick_room, name = "pick_room"),
]
