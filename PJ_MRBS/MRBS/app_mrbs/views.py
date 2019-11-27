from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse
from .templates import app_mrbs
from app_mrbs.models import Account

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
            # mix sud lhor
