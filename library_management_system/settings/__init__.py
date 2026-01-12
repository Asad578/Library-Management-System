"""
Settings package for library_management_system.
Import the appropriate settings module based on environment.
"""

import os
from decouple import config

# Get the environment from environment variable, default to 'dev'
ENVIRONMENT = config('DJANGO_ENV', default='dev')

if ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'staging':
    from .staging import *
else:
    from .development import *
