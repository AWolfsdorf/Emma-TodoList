from django.contrib import admin
from users import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    ordering = ['name']
# Register your models here.
admin.site.register(models.UserProfile,UserProfileAdmin)