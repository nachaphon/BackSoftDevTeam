from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse
from .templates import app_mrbs
from app_mrbs.models import Account, Day, Room, Timeslot ,RoomDay
# from .forms import Timeslotform

# Create your views here.

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'app_mrbs/index.html', context=None)

def homepage(request):
    return render(request, 'app_mrbs/home_page.html')


def check_account(request):
    if request.method == 'POST':
        IN_ID = request.POST.get('id')
        IN_PASSWORD = request.POST.get('password')
        all_account = Account.objects.all()

        for i in all_account:
            if IN_ID == i.username and IN_PASSWORD == i.password:
                context = {'username': i.username  }
                if i.status == "user":
                    return render(request,'app_mrbs/user_page.html',context)
                elif i.status == "admin":
                    return render(request,'app_mrbs/admin_page.html',context)
                break

        return render(request, 'app_mrbs/login_error.html', context=None)
    else:
        return HttpResponse("11111111111")

def admin(request):
    return HttpResponse("href=")

def sort_room(request):
    time = [12,30]
    seat = 10
    time_length = 3 # hr ไม่เกิน  4 hr
    result = []
    all_room = Timeslot.objects.all()

    result = []

  
    # for room in all_room:
    #     result1 = []
    #     if int(room.room_seat) >= seat:
    #         result1.append(room)
    #         for slot in all_timeslot:
    #             result1.append(slot[0])
    #         result.append(result1)


    context = {'result':result , 'all_room':all_room }

    return render(request, 'app_mrbs/sort.html', context)


def pick_day(request):
    all_day = Day.objects.all()
    context = {'all_day':all_day}
    return render(request, 'app_mrbs/pick_day.html', context)

def pick_room(request, day_id):
    day = get_object_or_404(Day, pk = day_id)
    # all_room = day.Room_set.all()
    thisday = RoomDay.objects.filter(day = day_id)
    all_slot_room1 = Timeslot.objects.filter(roomday = thisday[0])
    # all_slot = Timeslot.objects.filter(thisroom = day_id)
    # slot1 = all_slot
    # status1 = slot1.status1
    # if request.POST:
    #     if 'reserve' in request.POST:
    #         # timeslot1.status1 = 'full'
    #         slot1.status1 = 'full'
    #         slot1.save()
    #     elif 'cancel' in request.POST:
    #         slot1.status1 = 'empty'
    #         slot1.save()

    context = { 'day':day,
                'thisday':thisday,
                'all_slot':all_slot,}
                # 'slot1':slot1, }
                # 'status1':status1}
    return render(request, 'app_mrbs/pick_room.html', context)
