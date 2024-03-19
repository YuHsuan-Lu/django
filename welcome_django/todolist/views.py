from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Todolist
from project.models import Project
# Create your views here.

#pk here is todolist_id
@login_required
def todolist(request,project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)
    return render(request,'todolist/todolist.html',{
        'project':project,
        'todolist':todolist
    })




# 透過welcome_django/url內的 
# path('projects/<uuid:project_id>/',include('todolist.urls'))傳遞
@login_required
def add(request,project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    if request.method == 'POST':
        name = request.POST.get('name','')
        description = request.POST.get('description','')
        if name is not None:
            todolist = Todolist.objects.create(project=project,name=name,description=description,created_by=request.user)
            return redirect(f'/projects/{project_id}/')
    return render(request,'todolist/add.html',{
        'project':project
    })