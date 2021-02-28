"""
WSGI config for django_init project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
 
path = '/home/MiguelRiveraDev/aplicacion-inicio'
if path not in sys.path:
    sys.path.append(path)
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'aplicacion-inicio.settings'
 
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())