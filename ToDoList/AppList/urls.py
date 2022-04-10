from django.urls import path
from . import views

app_name = 'AppList'

urlpatterns = [
    path('', views.listar_tareas,name='index'),
]