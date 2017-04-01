"""
WSGI config for platform_simulation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

#WARNING ! --> Do not modify this file

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "platform_simulation.settings")

application = get_wsgi_application()
