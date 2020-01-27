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

# Replace the Invoice table with deterministic contents
Invoice.objects.all().delete()

incrementing_amount = 0.01
counter = 1
for i in range(1000):
    invoice = Invoice(
        id=counter,
        date=timezone.now(),
        amount=incrementing_amount,
        big=1000000 - counter
    )
    invoice.save()
    counter += 1
    incrementing_amount += 0.01

print("Finished")