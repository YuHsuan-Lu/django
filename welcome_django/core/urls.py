#it's better to have urls.py under each app
#this will generate path to views.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
]