"""
ASGI config for library_management_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from decouple import config

from django.core.asgi import get_asgi_application

# Set environment variable if not already set
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management_system.settings')

application = get_asgi_application()
