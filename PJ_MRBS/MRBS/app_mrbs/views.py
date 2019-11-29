from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse
from .templates import app_mrbs
from app_mrbs.models import Account, Day, Room, Timeslot
from .forms import Timeslotform

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
    all_room = Room.objects.all()
    
    for room in all_room:
        if int(room.room_seat) >= seat:
            result.append(room)

    context = {'result':result }

    return render(request, 'app_mrbs/sort.html', context)


def pick_day(request):
    all_day = Day.objects.all()
    context = {'all_day':all_day}
    return render(request, 'app_mrbs/pick_day.html', context)

def pick_room(request, day_id):
    day = get_object_or_404(Day, pk = day_id)
    # all_room = day.Room_set.all()
    all_room = Room.objects.filter(day = day_id)
    # room1 = all_room[0].Timeslot.objects.filter(room = all_room[0])
    # status1 = Timeslot.objects.filter(room = all_room[0])[0]['status1']
    status1 = Timeslot.objects.values('status1').filter(room = all_room[0])[0]['status1']
    # room1_name = room1.room_name()
    # for room in all_room:
    #     slot1 = Timeslot.objects.filter(room = room.id, slot = "1")
    # room1_slot1 =
    # form_room1_slot1 = Timeslot(request.POST or None)
    # if room1_slot1.is_valid():
    #     user_info.user_nam = form_room1_slot1.cleaned_data['status']
    #     user_info.save()
    timeslot1 = Timeslot.objects.filter(room = all_room[0])[0]
    status = timeslot1.status1
    # val = 'mix'
    # if request.method == 'POST':
    #     form = Fooform(request.POST)
    #     if form.is_valid():
    #         val = form.cleaned_data.get("btn")
    #         status1 = 'full'
    #         timeslot1.save()
    # else:
    #     form = Fooform()
    form = Timeslotform()
    # if form.is_valid():
    if request.POST:
        if 'reserve' in request.POST:
            timeslot1.status1 = 'full'
            timeslot1.save()
        elif 'cancel' in request.POST:
            timeslot1.status1 = 'empty'
            timeslot1.save()
    context = {'day':day, 'all_room':all_room, 'status1':status1, 'form':form, 'timeslot1':timeslot1, 'status':status}
    return render(request, 'app_mrbs/pick_room.html', context)
