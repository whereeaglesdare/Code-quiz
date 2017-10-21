# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 22:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_registration_profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]