# -*- coding: utf-8 -*-
'''
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
'''

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv


load_dotenv()


APP_ROOT_DIR_NAME = os.environ.get('APP_ROOT_DIR_NAME', 'app')

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    f'{APP_ROOT_DIR_NAME}.settings'
)

application = get_wsgi_application()
