from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse
from .templates import app_mrbs
from app_mrbs.models import Account, Day, Room

# Create your views here.

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'app_mrbs/index.html', context=None)


def check_account(request):
    if request.method == 'POST':
        IN_ID = request.POST.get('id')
        IN_PASSWORD = request.POST.get('password')
        ck_id = False
        all_account = Account.objects.all()

        for i in all_account:
            if IN_ID == i.user_name and IN_PASSWORD == i.password:
                ck_id = True
                return render(request,'app_mrbs/user.html')
                break

        return render(request,'app_mrbs/index.html')
    else:
        return HttpResponse()

def pick_day(request):
    all_day = Day.objects.all()
    context = {'all_day':all_day}
    return render(request, 'app_mrbs/pick_day.html', context)

def pick_room(request, day_id):
    day = get_object_or_404(Day, pk = day_id)
    # all_room = day.Room_set.all()
    all_room = Room.objects.filter(day = day_id)
    context = {'day':day, 'all_room':all_room}
    return render(request, 'app_mrbs/pick_room.html', context)
