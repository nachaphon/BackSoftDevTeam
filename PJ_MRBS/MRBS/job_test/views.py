# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'index.html', context=None)
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        context = {
            'name':name,
            'email':email,
            'phone':phone
        }
        template = loader.get_template('result.html')

        return HttpResponse(template.render(context,request))

    else :
            #if post request is not true
            #returning the form template
            template = loader.get_template('index.html')
            return HttpResponse(template.render())

def aa(request):
    return HttpResponse("<h1>JOB<h1>")