from __future__ import absolute_import
from .base import *


ALLOWED_HOSTS = ('0.0.0.0', '127.0.0.1', 'localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'local',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

if DEBUG:
    from .base import MIDDLEWARE_CLASSES, INSTALLED_APPS
    # INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'localhost')
    DJANGO_APPS = (
        'debug_toolbar',
    )
    THIRD_PARTY_APPS = ()
    LOCAL_APPS = (

    )
    INSTALLED_APPS += DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    DEBUG_TOOLBAR_PATCH_SETTINGS = True
