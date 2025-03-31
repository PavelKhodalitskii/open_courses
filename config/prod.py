from .settings import *

DEBUG = False
PRODUCTION = True

ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': os.getenv('POSTGRES_OUT_PORT'),
    }
}

STATIC_URL = ''
STATIC_ROOT = ''

MEDIA_URL = ''
MEDIA_ROOT = ''