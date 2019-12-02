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

def homepage2(request):
    return render(request, 'app_mrbs/base0.html')


def check_account(request):
    if request.method == 'POST':
        IN_ID = request.POST.get('id')
        IN_PASSWORD = request.POST.get('password')
        all_account = Account.objects.all()

        for i in all_account:
            if IN_ID == i.username and IN_PASSWORD == i.password:
                context = {'username': i.username  }
                if i.status == "user":
                    request.session['user_name'] = IN_ID
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
    time_length_hr = 1 # hr ไม่เกิน  4 hr
    time_length_min = 30 # min
    if time_length_min == 30:
        time_length_min = 1
    slot_length = (time_length_hr*2) + time_length_min
    all_room = Timeslot.objects.all()[(day*5)-5:(day*5)]

    result = []
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
        result_ = []
        if int(all_room[i].roomday.room.room_seat) > seat:
            count_slot_empty = 0
            count_slot = 0
            r_slot = []
            for j in all_slot[i]:
                count_slot += 1
                if j == "empty":
                    count_slot_empty += 1
                    r_slot.append(count_slot)
                else:
                    count_slot_empty = 0
                    r_slot = []
                if count_slot_empty >= slot_length:
                    result_slot.append(r_slot)
                    result_room.append(all_room[i])
                    result_.append(all_room[i])
                    result_.append(r_slot)
                    result.append(result_)
                    break



    context = {'result_room':result_room ,
               'all_room':all_room ,
               'slot_length':slot_length,
               'seat':seat,
               'len_result_room':len(result_room),
               'result_slot':result_slot,
               'result':result,


            }

    return render(request, 'app_mrbs/sort.html', context)


def pick_day(request):
    all_day = Day.objects.all()
    context = {'all_day':all_day}
    return render(request, 'app_mrbs/pick_day.html', context)

def pick_room(request, day_id):
    day = get_object_or_404(Day, pk = day_id)
    thisday = RoomDay.objects.filter(day = day_id) #เอาทุกห้องของวันนี้มา
    all_slot_room1 = Timeslot.objects.filter(roomday = thisday[0])[0] #เอาslotของห้องที่ 1 ของวันนี้มา
    #ต้องใส้ [0] ตรงท้ายสุดด้วย เพราะ เราเรียก timeslot ตัวเเรกของ room นั้นออกมา
    all_slot_room2 = Timeslot.objects.filter(roomday = thisday[1])[0]
    all_slot_room3 = Timeslot.objects.filter(roomday = thisday[2])[0]
    all_slot_room4 = Timeslot.objects.filter(roomday = thisday[3])[0]
    all_slot_room5 = Timeslot.objects.filter(roomday = thisday[4])[0]
    slot1 = all_slot_room1.status1
    room_list = [all_slot_room1, all_slot_room2, all_slot_room3, all_slot_room4, all_slot_room5]
    # status1 = slot1.status1
    reserve_slot1 = []
    for i in range(1, 66, 16):
        reserve_slot1.append(str(i))
    reserve_slot2 = []
    for i in range(2, 67, 16):
        reserve_slot2.append(str(i))
    reserve_slot3 = []
    for i in range(3, 68, 16):
        reserve_slot3.append(str(i))
    reserve_slot4 = []
    for i in range(4, 69, 16):
        reserve_slot4.append(str(i))
    reserve_slot5 = []
    for i in range(5, 70, 16):
        reserve_slot5.append(str(i))
    reserve_slot6 = []
    for i in range(6, 71, 16):
        reserve_slot6.append(str(i))
    reserve_slot7 = []
    for i in range(7, 72, 16):
        reserve_slot7.append(str(i))
    reserve_slot8 = []
    for i in range(8, 73, 16):
        reserve_slot8.append(str(i))
    reserve_slot9 = []
    for i in range(9, 74, 16):
        reserve_slot9.append(str(i))
    reserve_slot10 = []
    for i in range(10, 75, 16):
        reserve_slot10.append(str(i))
    reserve_slot11 = []
    for i in range(11, 76, 16):
        reserve_slot11.append(str(i))
    reserve_slot12 = []
    for i in range(12, 77, 16):
        reserve_slot12.append(str(i))
    reserve_slot13 = []
    for i in range(13, 78, 16):
        reserve_slot13.append(str(i))
    reserve_slot14 = []
    for i in range(14, 79, 16):
        reserve_slot14.append(str(i))
    reserve_slot15 = []
    for i in range(15, 80, 16):
        reserve_slot15.append(str(i))
    reserve_slot16 = []
    for i in range(16, 81, 16):
        reserve_slot16.append(str(i))

    cancel_slot1 = []
    for i in range(81, 146, 16):
        cancel_slot1.append(str(i))
    cancel_slot2 = []
    for i in range(82, 147, 16):
        cancel_slot2.append(str(i))
    cancel_slot3 = []
    for i in range(83, 148, 16):
        cancel_slot3.append(str(i))
    cancel_slot4 = []
    for i in range(84, 149, 16):
        cancel_slot4.append(str(i))
    cancel_slot5 = []
    for i in range(85, 150, 16):
        cancel_slot5.append(str(i))
    cancel_slot6 = []
    for i in range(86, 151, 16):
        cancel_slot6.append(str(i))
    cancel_slot7 = []
    for i in range(87, 152, 16):
        cancel_slot7.append(str(i))
    cancel_slot8 = []
    for i in range(88, 153, 16):
        cancel_slot8.append(str(i))
    cancel_slot9 = []
    for i in range(89, 154, 16):
        cancel_slot9.append(str(i))
    cancel_slot10 = []
    for i in range(90, 155, 16):
        cancel_slot10.append(str(i))
    cancel_slot11 = []
    for i in range(91, 156, 16):
        cancel_slot11.append(str(i))
    cancel_slot12 = []
    for i in range(92, 157, 16):
        cancel_slot12.append(str(i))
    cancel_slot13 = []
    for i in range(93, 158, 16):
        cancel_slot13.append(str(i))
    cancel_slot14 = []
    for i in range(94, 159, 16):
        cancel_slot14.append(str(i))
    cancel_slot15 = []
    for i in range(95, 160, 16):
        cancel_slot15.append(str(i))
    cancel_slot16 = []
    for i in range(96, 161, 16):
        cancel_slot16.append(str(i))

    user_name = request.session.get('user_name')

    if request.POST:
        for i in range(1, 161):
            if str(i) in request.POST:
                if  1 <= i <= 16 or 81 <= i <= 96:
                    preRoomSelect = room_list[0]
                elif  17 <= i <= 32 or 97 <= i <= 112:
                    preRoomSelect = room_list[1]
                elif  33 <= i <= 48 or 113 <= i <= 128:
                    preRoomSelect = room_list[2]
                elif  49 <= i <= 64 or 129 <= i <= 144:
                    preRoomSelect = room_list[3]
                elif  65 <= i <= 80 or 145 <= i <= 160:
                    preRoomSelect = room_list[4]
                # all_slot_room1.status1 = 'full'
                if str(i) in reserve_slot1:
                    if preRoomSelect.status1 == 'empty':
                        preRoomSelect.status1 = 'full'
                        preRoomSelect.user1 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot2:
                    if preRoomSelect.status2 == 'empty':
                        preRoomSelect.status2 = 'full'
                        preRoomSelect.user2 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot3:
                    if preRoomSelect.status3 == 'empty':
                        preRoomSelect.status3 = 'full'
                        preRoomSelect.user3 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot4:
                    if preRoomSelect.status4 == 'empty':
                        preRoomSelect.status4 = 'full'
                        preRoomSelect.user4 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot5:
                    if preRoomSelect.status5 == 'empty':
                        preRoomSelect.status5 = 'full'
                        preRoomSelect.user5 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot6:
                    if preRoomSelect.status6 == 'empty':
                        preRoomSelect.status6 = 'full'
                        preRoomSelect.user6 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot7:
                    if preRoomSelect.status7 == 'empty':
                        preRoomSelect.status7 = 'full'
                        preRoomSelect.user7 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot8:
                    if preRoomSelect.status8 == 'empty':
                        preRoomSelect.status8 = 'full'
                        preRoomSelect.user8 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot9:
                    if preRoomSelect.status9 == 'empty':
                        preRoomSelect.status9 = 'full'
                        preRoomSelect.user9 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot10:
                    if preRoomSelect.status10 == 'empty':
                        preRoomSelect.status10 = 'full'
                        preRoomSelect.user10 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot11:
                    if preRoomSelect.status11 == 'empty':
                        preRoomSelect.status11 = 'full'
                        preRoomSelect.user11 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot12:
                    if preRoomSelect.status12 == 'empty':
                        preRoomSelect.status12 = 'full'
                        preRoomSelect.user12 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot13:
                    if preRoomSelect.status13 == 'empty':
                        preRoomSelect.status13 = 'full'
                        preRoomSelect.user13 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot14:
                    if preRoomSelect.status14 == 'empty':
                        preRoomSelect.status14 = 'full'
                        preRoomSelect.user14 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot15:
                    if preRoomSelect.status15 == 'empty':
                        preRoomSelect.status15 = 'full'
                        preRoomSelect.user15 = user_name
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in reserve_slot16:
                    if preRoomSelect.status16 == 'empty':
                        preRoomSelect.status16 = 'full'
                        preRoomSelect.user16 = user_name
                        preRoomSelect.save()
                    else:
                        break
                # elif str(i) in request.POST:
                #     all_slot_room1.status1 = 'empty'
                #     all_slot_room1.save()
                elif str(i) in cancel_slot1:
                    if preRoomSelect.user1 == user_name:
                        preRoomSelect.status1 = 'empty'
                        preRoomSelect.user1 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot2:
                    if preRoomSelect.user2 == user_name:
                        preRoomSelect.status2 = 'empty'
                        preRoomSelect.user2 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot3:
                    if preRoomSelect.user3 == user_name:
                        preRoomSelect.status3 = 'empty'
                        preRoomSelect.user3 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot4:
                    if preRoomSelect.user4 == user_name:
                        preRoomSelect.status4 = 'empty'
                        preRoomSelect.user4 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot5:
                    if preRoomSelect.user5 == user_name:
                        preRoomSelect.status5 = 'empty'
                        preRoomSelect.user5 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot6:
                    if preRoomSelect.user6 == user_name:
                        preRoomSelect.status6 = 'empty'
                        preRoomSelect.user6 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot7:
                    if preRoomSelect.user7 == user_name:
                        preRoomSelect.status7 = 'empty'
                        preRoomSelect.user7 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot8:
                    if preRoomSelect.user8 == user_name:
                        preRoomSelect.status8 = 'empty'
                        preRoomSelect.user8 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot9:
                    if preRoomSelect.user9 == user_name:
                        preRoomSelect.status9 = 'empty'
                        preRoomSelect.user9 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot10:
                    if preRoomSelect.user10 == user_name:
                        preRoomSelect.status10 = 'empty'
                        preRoomSelect.user10 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot11:
                    if preRoomSelect.user11 == user_name:
                        preRoomSelect.status11 = 'empty'
                        preRoomSelect.user11 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot12:
                    if preRoomSelect.user12 == user_name:
                        preRoomSelect.status12 = 'empty'
                        preRoomSelect.user12 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot13:
                    if preRoomSelect.user13 == user_name:
                        preRoomSelect.status13 = 'empty'
                        preRoomSelect.user13 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot14:
                    if preRoomSelect.user14 == user_name:
                        preRoomSelect.status14 = 'empty'
                        preRoomSelect.user14 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot15:
                    if preRoomSelect.user15 == user_name:
                        preRoomSelect.status15 = 'empty'
                        preRoomSelect.user15 = 'none'
                        preRoomSelect.save()
                    else:
                        break
                elif str(i) in cancel_slot16:
                    if preRoomSelect.user16 == user_name:
                        preRoomSelect.status16 = 'empty'
                        preRoomSelect.user16 = 'none'
                        preRoomSelect.save()
                    else:
                        break
    list_status = [all_slot_room1.status1, all_slot_room1.status2]
    list_number = [0, 1]
    context = { 'day':day,
                'thisday':thisday,
                'all_slot_room1':all_slot_room1,
                'slot1':slot1,
                'list_status':list_status,
                'list_number':list_number }
                # 'status1':status1}
    return render(request, 'app_mrbs/pick_room.html', context)
