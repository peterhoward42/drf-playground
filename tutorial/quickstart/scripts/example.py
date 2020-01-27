"""
Demonstrates the form for a standalone scripts that can run in
the Django environment - without being run via manage.py
"""

import os
import sys
from pathlib import Path
from datetime import datetime

from django.core.wsgi import get_wsgi_application

# Where are we?
scripts_dir = os.path.dirname(__file__)
apps_path = Path(scripts_dir).parent
proj_path = apps_path.parent

# Set the DJANGO_SETTINGS_MODULE environment variable
settings_module = f"{proj_path.name}.settings"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

# Add project directory to python path
sys.path.append(str(proj_path))

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