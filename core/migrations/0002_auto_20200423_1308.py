# Generated by Django 3.0.4 on 2020-04-23 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='cellphone_no',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
