from django.http import response
from django.shortcuts import render,HttpResponseRedirect
import requests
from . api import  extreact_data
from .models import platform
from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
import io


def home(request):
    all_platform={}
    url="https://libraries.io/api/platforms"

    response = requests.get(url)
    data = response.json()
    for i  in data:
        con=platform(
            name=i['name'],
            project_count=i['project_count'],
            homepage=i['homepage'],
            color=i['color'],
            # default_language=i['default_language'],

        )
        con.save()
        all_platform=platform.objects.all().order_by('-id')

   
    return render(request, 'base.html',{'all_platform':all_platform})





def index(request):


    return render(request, 'index.html',) 






# def home(request):

#     return render(request, 'base.html',)