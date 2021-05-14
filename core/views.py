from typing import List
from django import views
from django.http import response
from django.shortcuts import redirect, render, HttpResponse
import requests
from requests.api import get
from .api import api_endpoint
import io
import os
from django.http import JsonResponse
from urllib.parse import urlencode
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.translation import gettext

from django.http import HttpResponse
from django.views.generic import TemplateView  # import the TemplateView parent class

from django.urls import reverse_lazy

api_key = os.getenv("api_key")

# platform="npm"
# name="react"

# class ShowTimeView(TemplateView):  # extend from TemplateView
    # template_name = 'github.html'  # add a template_name attribute
     
    
def get_context_data(request):
    path ="/api/github/gruntjs/grunt/dependencies"
    pathprojects = "/api/github/gruntjs/grunt/projects"


    a = api_endpoint.url(path)
    a_pathprojects = api_endpoint.url(pathprojects)
# 


    content = {
        'respons': a,
        'project':a_pathprojects,
        
    }
    return render(request, "github.html", content)



    
#     return render(request, self.template_name, content)
# def dependents(self, request, *args, **kwargs):
#     dependents = "/api/github/gruntjs/grunt/dependents"

    #     respons = api_endpoint.url(dependents)
    #     content = {
    #         'dependents': respons
    #     }
    #     return render(request, self.template_name, content)

    # def dependent_repositories(self, request, *args, **kwargs):

    #     dependent_repositories = "/api/github/gruntjs/grunt/dependent_repositories"

    #     respons = api_endpoint.url(dependent_repositories)
    #     content = {
    #         'dependent_repositories': respons
    #     }
    #     return render(request, self.template_name, content)

    # def contributors(self, request, *args, **kwargs):

    #     contributors = "/api/github/gruntjs/grunt/contributors"

    #     respons = api_endpoint.url(contributors)
    #     content = {
    #         'contributors': respons
    #     }
    #     return render(request, self.template_name, content)

    # def contributors(self, request, *args, **kwargs):

    #     contributors = "/api/github/gruntjs/grunt/sourcerank"

    #     respons = api_endpoint.url(contributors)
    #     content = {
    #         'contributors': respons
    #     }
    #     return render(request, self.template_name, content)

    #     # return JsonResponse(content)

def home(request):

    return render(request, 'base.html')


def blog(request):

    return render(request, 'blog.html')


def index(request):
   

    # return  post_id
    path = '/api/platforms'
    # api_key='YOUR_API_KEY'
    payload = {
        # 'q': 'a',
        # 'b': 'a',
        'api_key': api_key,
    }
    query = urlencode(payload)
    con = api_endpoint.base_url(path, query)
    a=gettext(con)
    content = {
        'con':a }
    return render(request, 'index.html', content)
    # return JsonResponse(content)

    # return render(request, 'index.html',content)


def api_search(request):

    
    short= request.GET.get('short')
    sea_id = request.GET.get('value')
    # redirect("/apierach")
    print(short)
    print(sea_id)
    
    


    path = '/api/search'
    payload = {
        'q':sea_id,
        'sort':short,
        'api_key': api_key,
    }
    query = urlencode(payload)
    conme = api_endpoint.base_url(path, query)

    # response={
    #     a:conme,
    # }
    # # print(conme)

    return HttpResponse(conme)

    # return render(request, 'PlatformDetail.html',{'conme':conme})

# class SignUpView():
#     template_name = 'signup.html'
#     success_url = reverse_lazy('home')
