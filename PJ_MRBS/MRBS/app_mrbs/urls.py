from django.urls import path
from app_mrbs import views

urlpatterns = [
    # path('',views.HomePageView.as_view() , name= 'home-page'),
    path('',views.homepage , name= 'home-page'),
    path('/admin-page',views.admin , name= 'admin-page'),
    # path('check_account/',views.check_account ,name='ck'),
    
]
