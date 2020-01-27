#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from django.core.wsgi import get_wsgi_application
#from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# derive location to your django project setting.py
proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings'
                      )
sys.path.append(proj_path)
# load your settings.py
os.chdir(proj_path)
# In essence you are actually loading up all the django components and settings
# so we gain access to djangos ORM
application = get_wsgi_application()
# run your custom script here
def create_or_update_admin_users():
    if settings.ADMINS:
        for django_admin_user in settings.ADMINS:
            try:
                user = User.objects.get(email=django_admin_user[1])
            except User.DoesNotExist:
                user = User()
            user.username = django_admin_user[1]
            user.set_password('admin123')
            user.first_name = str(django_admin_user[0]).split()[0]
            user.last_name = str(django_admin_user[0]).split()[1]
            user.email = django_admin_user[1]
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.date_joined = timezone.now()
            user.save()
create_or_update_admin_users()