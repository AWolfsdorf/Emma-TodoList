# Generated by Django 3.2.6 on 2022-04-10 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppList', '0002_alter_task_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-pub_date']},
        ),
    ]