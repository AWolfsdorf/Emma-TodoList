# Generated by Django 3.2.6 on 2022-04-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
