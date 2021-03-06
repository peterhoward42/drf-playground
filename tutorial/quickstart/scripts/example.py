"""
Demonstrates the form for a standalone scripts that can run in
the Django environment - without being run via manage.py

Based on https://medium.com/@django.course/run-django-as-a-standalone-python-script-a81912815276
"""

import os
import sys
from pathlib import Path
from datetime import datetime

from django.core.wsgi import get_wsgi_application

# Where are we?
scripts_dir = os.path.dirname(__file__)
app_dir = os.path.abspath(os.path.join(scripts_dir, '..'))
proj_dir = os.path.abspath(os.path.join(app_dir, '..'))
repo_dir = os.path.abspath(os.path.join(proj_dir, '..'))

# Set dependencies for get_wsgi_application()
sys.path.append(str(repo_dir))

print(f"XXXXX sys.path: {sys.path}\n")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "tutorial.settings")

# Initialise the django app - which loads the the settings module, and
# initialises database client etc.
application = get_wsgi_application()

# Only now can importing a model class succeed - because it  raises exceptions if the app
# is not yet initialised.
from tutorial.quickstart.models import Invoice

invoice = Invoice(
    date=datetime.now(),
    amount=99.9
)