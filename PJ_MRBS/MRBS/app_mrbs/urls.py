from django.urls import path
from app_mrbs import views

app_name = 'mrbs'

urlpatterns = [
<<<<<<< HEAD
    # path('',views.HomePageView.as_view() , name= 'home-page'),
    path('',views.homepage , name= 'home-page'),
    path('/admin-page',views.admin , name= 'admin-page'),
    # path('check_account/',views.check_account ,name='ck'),
    
=======
    path('',views.HomePageView.as_view()),
    path('user/',views.check_account),
    path('user/pick_day',views.pick_day, name = "pick_day"),
    path('user/pick_day/pick_room/<int:day_id>',views.pick_room, name = "pick_room"),
>>>>>>> 9b5f5aea0b0cbf4e682344fe37aa9f32203fa403
]
