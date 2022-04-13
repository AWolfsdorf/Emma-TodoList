
from cProfile import label
from django.db import models
from django.utils import timezone
import datetime
from django import forms
from django.urls import reverse
from users.models import *

status_task =(
                ('E1' , 'Pendiente'),
                ('E2' , 'En proceso'),
                ('E3' , 'Realizada')
            )

class Task(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=50, default='x')
    task_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    state = models.CharField(max_length=2, choices=status_task, default='E1')

    def __str__(self):
        return self.task_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-pub_date']


