
from django.http import HttpRequest, HttpResponseRedirect

from django.contrib import admin
from .models import UserProfile 
from django.views import generic
from django.shortcuts import render
from django.views import View
from .models import Task
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# # Create your views here.

# class IndexView(generic.ListView):
#     model = UserProfile
#     template_name = 'AppList/index.html'
#     # Agregando la siguiente linea le cambias el nombre del 'object_list'
#     context_object_name = 'user_profiles'

#     def get(self, request):
#         print(request.user)
#         return HttpResponse()

def is_loged(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return False
    return True


class MyViews(HttpRequest):
    def listar_tareas(request):
        if is_loged(request):
            # UserProfiles= UserProfile.objects.all()
            UserProfiles= UserProfile.objects.get(email=request.user.get_username())
            return render(request,"../templates/AppList/listarTareas.html",{"request":request,"perfilDeUsuario": UserProfiles})
        else:
            return HttpResponseRedirect("/admin/")