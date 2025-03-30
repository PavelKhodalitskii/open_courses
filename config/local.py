from .settings import *

DEBUG = True
PRODUCTION = False

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost', 'http://localhost:9000']

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

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')