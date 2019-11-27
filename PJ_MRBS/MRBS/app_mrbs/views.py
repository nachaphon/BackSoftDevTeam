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


def homepage(request):
    if request.method == 'POST':
        IN_ID = request.POST.get('id')
        IN_PASSWORD = request.POST.get('password')
        all_account = Account.objects.all()

        for i in all_account:
            if IN_ID == i.username and IN_PASSWORD == i.password:
                context = {'username': i.username  }
                if i.status == "user":
                    return render(request,'app_mrbs/user.html',context)
                elif i.status == "admin":
                    return render(request,'app_mrbs/admin_page.html',context)
                break

        return render(request, 'app_mrbs/login_error.html')
    else:
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
                    return render(request,'app_mrbs/user.html',context)
                elif i.status == "admin":
                    return render(request,'app_mrbs/admin_page.html',context)
                break

        return render(request, 'app_mrbs/index.html', context=None)
    else:
        return HttpResponse("11111111111")

def admin(request):
    return HttpResponse("<h2>job<h2>")