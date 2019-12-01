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
    day = 1
    time = [12,30]
    seat = 8
    time_length_hr = 3 # hr ไม่เกิน  4 hr
    time_length_min = 30 # min
    if time_length_min == 30:
        time_length_min = 1
    slot_length = (time_length_hr*2) + time_length_min
    all_room = Timeslot.objects.all()[(day*5)-5:(day*5)]

    result_room = []
    result_slot = []

    all_slot = []
    for i in all_room:
        r1 = []
        r1.append(i.status1)
        r1.append(i.status2)
        r1.append(i.status3)
        r1.append(i.status4)
        r1.append(i.status5)
        r1.append(i.status6)
        r1.append(i.status7)
        r1.append(i.status8)
        r1.append(i.status9)
        r1.append(i.status10)
        r1.append(i.status11)
        r1.append(i.status12)
        r1.append(i.status13)
        r1.append(i.status14)
        r1.append(i.status15)
        r1.append(i.status16)
        all_slot.append(r1)


  
    for i in range(len(all_room)):
        if int(all_room[i].roomday.room.room_seat) > seat:
            count_slot_empty = 0
            r_slot = []
            for j in all_slot[i]:
                if j == "empty":
                    count_slot_empty += 1
                    result_slot.append(j)
                else:
                    count_slot_empty = 0
                    r_slot = []
                if count_slot_empty >= slot_length:
                    result_slot.append(r_slot)
                    result_room.append(all_room[i])
                    break



    context = {'result_room':result_room ,
               'all_room':all_room ,
               'slot_length':slot_length,
               'seat':seat,
               'len_result_room':len(result_room),
               'result_slot':result_slot,


            }

    return render(request, 'app_mrbs/sort.html', context)


def pick_day(request):
    all_day = Day.objects.all()
    context = {'all_day':all_day}
    return render(request, 'app_mrbs/pick_day.html', context)

def pick_room(request, day_id):
    day = get_object_or_404(Day, pk = day_id)
    thisday = RoomDay.objects.filter(day = day_id) #เอาทุกห้องของวันนี้มา
    all_slot_room1 = Timeslot.objects.filter(roomday = thisday[0]) #เอาslotของห้องที่ 1 ของวันนี้มา
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
                'all_slot_room1':all_slot_room1,}
                # 'slot1':slot1, }
                # 'status1':status1}
    return render(request, 'app_mrbs/pick_room.html', context)
