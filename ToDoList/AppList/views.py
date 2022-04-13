
from django.shortcuts import render , redirect
from users.models import UserProfile 
from AppList.models import Task
from AppList import models
from ToDoList.functions import *
from django.contrib import messages
from django.utils.translation import gettext, gettext_lazy as _
from AppList.forms import TaskForm
from django.contrib.auth.decorators import login_required

def Home_App(request):
    if is_loged(request):
        user_profiles= UserProfile.objects.get(email=request.user.get_username())
        
        return render(request,"AppList/HomeApp.html",{"request":request,"perfilDeUsuario": user_profiles})
    else:
        login_msg =_(f'You have to log in to use the app')
        messages.warning(request ,login_msg)
        return render(request,"AppList/HomeApp.html",{'login_msg':login_msg})

def About_App(request):
    return render(request,"AppList/about.html")





# Create your views here.
@login_required
def TaskAdd_View(request):
    title_page = _('Add Task')
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task()
            new_task.task_title = form.cleaned_data.get('task_title')
            new_task.task_text = form.cleaned_data.get('task_text')
            new_task.state = form.cleaned_data.get('state')
            new_task.user = request.user
            new_task.save()
            text_msg =_(f'Task "{new_task.task_title}" added successfully')
            messages.success(request ,text_msg)
            return redirect('homeapp')
    else:
        form = TaskForm()
    return render(request,'AppList/task_form.html',{'form':form,'title': title_page})

@login_required
def TaskEdit_View(request):
    title_page = _('Edit Task')
    ID_TASK =''
    ID_TASK = request.GET.get('id_task')
    if request.method =='POST':
        object = Task.objects.get(pk=ID_TASK)
        form = TaskForm(request.POST , instance=object)
        if form.is_valid():
            form.save()
            text_msg =_(f'Task "{object.task_title}" edited successfully')
            messages.success(request ,text_msg)
            return redirect('homeapp')
    elif request.method =='GET':
        editObject = Task.objects.get(pk=ID_TASK)
        form = TaskForm(instance=editObject)
        return render(request,'AppList/task_form.html',{'form':form,'title': title_page})
    return redirect('homeapp')


@login_required
def TaskDelete_View(request):
    ID_TASK =''
    ID_TASK = request.GET.get('id_task')
    if request.method =='GET':
        deleteObject = Task.objects.get(pk=ID_TASK)
        deleteObject.delete()
        text_msg =_(f'Task "{deleteObject.task_title}" deleted successfully')
        messages.warning(request ,text_msg)
        return redirect('homeapp')
    return redirect('homeapp')