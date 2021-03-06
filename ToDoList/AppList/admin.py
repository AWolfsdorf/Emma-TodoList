from django.contrib import admin

from AppList import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ['user','pub_date','task_title','task_text', 'state']
    ordering = ['pub_date']


# Register your models here.
admin.site.register(models.Task,TaskAdmin)
admin.site.site_header = "Aplicacion de listas de tareas"
admin.site.site_title = "Admin App listas de tareas"
admin.site.index_title = "Admin App listas de tareas"