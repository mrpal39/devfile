from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('api_search/', views.api_search, name='api_search'),
    path('blog/', views.blog, name='blog'),

    path('github/', views.get_context_data, name='github'),

]
