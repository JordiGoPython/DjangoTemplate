from os.path import abspath, basename, dirname, join, normpath, realpath
from sys import path

SETTINGS_DIR = realpath(dirname(__file__)).replace('\\', '/')
DJANGO_ROOT = dirname(dirname(abspath(__file__))).replace('\\', '/')
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)
SITE_DOMAIN = '%s.com' % SITE_NAME.lower()
path.append(DJANGO_ROOT)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    ('jordi', 'jtantadiaz@gmail.com'),
)
MANAGERS = ADMINS

SECRET_KEY = 'z@)$q6%rl@d$b5m2)jt4pro$p&&42@-=uku794we5)6!fr4vj('

DEBUG = False


ALLOWED_HOSTS = []

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'apps.test1',
    'apps.core',
    'apps.test2',

)
THIRD_PARTY_APPS = (

)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'apps.core.middleware.thread_user.CuserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Test.urls'
WSGI_APPLICATION = 'config.wsgi.application'
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'


STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (normpath(join(SITE_ROOT, 'templates')),),
        'APP_DIRS': True,
        'DEBUG': DEBUG,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'apps.core.processors.context_processors.base_url',
            ],
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'core.User'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'



