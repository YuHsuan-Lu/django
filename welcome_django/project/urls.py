from django.urls import path
from . import views
app_name = 'project'

urlpatterns = [
    path('', views.projects, name = 'projects'),#此處'projects/'換在welcome_django/urls.py底下定義
    path('add/', views.add, name = 'add'),
    path('<uuid:pk>', views.project, name = 'project'),
    path('<uuid:pk>/edit/', views.edit, name = 'edit'),
    path('<uuid:pk>/delete/', views.delete, name = 'delete'),
]