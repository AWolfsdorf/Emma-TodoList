from django.shortcuts import render , redirect

from django.contrib import messages
from ToDoList.functions import *
from .forms import UserRegisterForm 
from .models import UserProfile

from django.utils.translation import gettext, gettext_lazy as _

# Create your views here.
def register(request):
    if not is_loged(request):
        if request.method =='POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                new_user = UserProfile()
                new_user.email = form.cleaned_data.get('email')
                username = new_user.name = form.cleaned_data.get('name')
                new_user.password = form.cleaned_data.get('password')
                new_user.set_password(new_user.password)
                new_user.save()

                text_msg =_(f'Account created for {username}!')
                messages.success(request ,text_msg)
                return redirect('homeapp')
        else:
            form = UserRegisterForm()
        return render(request,'users/register.html',{'form':form})
    else:
        return redirect('homeapp')

# def login(request):
#     if not is_loged(request):
#         if request.method =='POST':
#             form = UserLoginForm(request.POST)
#             if form.is_valid():
#                 user = authenticate(username=form.cleaned_data.get('name'), password=form.cleaned_data.get('password'))
#                 if user is not None:
#                     # A backend authenticated the credentials
#                 else:

#                 return redirect('homeapp')
#             else:
#                 form = UserLoginForm()
#                 return render(request,'users/login.html',{'form':form})
#     else:
#         return redirect('homeapp')
