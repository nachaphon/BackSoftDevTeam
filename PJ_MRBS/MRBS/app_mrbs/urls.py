from django.urls import path
from app_mrbs import views

app_name = 'mrbs'

urlpatterns = [
    # path('',views.HomePageView.as_view() , name= 'home-page'),
    path('',views.homepage , name= 'home-page'),
    path('admin_page/',views.admin , name= 'admin-page'),
    path('user_page/',views.user , name= 'user-page'),
    path('account/',views.check_account ,name='ck'),
    path('sort/',views.sort_room ,name='sort'),
    path('bookingForSort/',views.booking_sort_room ,name='bookingforsort'),
    
    path('sortmix/',views.sort_mix ,name='sortmix'),
    path('user/pick_day',views.pick_day, name = "pick_day"),
    path('user/pick_day/pick_room/<int:day_id>',views.pick_room, name = "pick_room"),
    path('base0',views.homepage2, name = "base0"),
]
