

from django.forms.models import ModelForm
from django import forms
from AppList import models
from AppList.models import Task
from django.utils.translation import gettext, gettext_lazy as _


class TaskForm(ModelForm):

    # user = forms.CharField(
    #     label=_("user").capitalize,
    #     widget=forms.TextInput()
    # )
    task_title = forms.CharField(
        label=_("task title").capitalize,
        widget=forms.TextInput()
    )
    task_text = forms.CharField(
        label=_("task text").capitalize,
        widget=forms.Textarea()
    )

    # pub_date = forms.DateTimeField(
    #     label=_("date published"),
    #     widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local'},format="%Y-%m-%d %H:%M:%S")
    # )

    state= forms.ChoiceField(
        label=_("state").capitalize,
        choices=models.status_task
    )
    

    class Meta:
        model = Task
        fields = ['task_title','task_text','state']
       
