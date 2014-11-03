"""
WSGI config for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from os.path import abspath, dirname
from sys import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fortytwo.settings")

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
