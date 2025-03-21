"""
WSGI config for ldsym project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ldsym.settings')

application = get_wsgi_application()
# api/wsgi.py
app = get_wsgi_application()
