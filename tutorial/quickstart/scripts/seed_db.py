"""
A standalone program to populate the database.
"""

import os
import sys
from pathlib import Path

from django.utils import timezone
from django.core.wsgi import get_wsgi_application

# Where are we?
scripts_dir = os.path.dirname(__file__)
app_dir = os.path.abspath(os.path.join(scripts_dir, '..'))
proj_dir = os.path.abspath(os.path.join(app_dir, '..'))
repo_dir = os.path.abspath(os.path.join(proj_dir, '..'))

# Set dependencies for get_wsgi_application()
sys.path.append(str(repo_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "tutorial.settings")

# Initialise the django app - which loads the the settings module, and
# initialises database client etc.
application = get_wsgi_application()

# Only now can importing a model class succeed - because it  raises exceptions if the app
# is not yet initialised.
from tutorial.quickstart.models import Invoice

for i in range(3):
    invoice = Invoice(
        date=timezone.now(),
        amount=99.9
    )
    invoice.save()

print("Finished")