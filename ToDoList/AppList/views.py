
from django.http import HttpResponseRedirect

from .models import UserProfile 

from django.shortcuts import render

# # Create your views here.

def is_loged(request):
  
    if not request.user.is_authenticated:
        return False
    return True



def listar_tareas(request):
    if is_loged(request):
        user_profiles= UserProfile.objects.get(email=request.user.get_username())
        return render(request,"../templates/AppList/listarTareas.html",{"request":request,"perfilDeUsuario": user_profiles})
    else:
        return HttpResponseRedirect("/admin/")