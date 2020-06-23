import os
import dj_database_url
from .base_settings import *

ALLOWED_HOSTS = [
    'myproj.dev.expandshare.com',
    'myproj.prod.expandshare.com',
]
DATABASES['default'] = dj_database_url.config() if os.environ.get('DATABASE_URL') else DATABASES['default']
DEBUG = False
MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
INSTALLED_APPS += [
    # Third-party apps
    'corsheaders',
    'rest_framework',

    # Custom apps
    'polls',
    'tenants',
]

# Static Files + Media Configuration
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'myproj', 'media')
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# django-cors-headers settings
from myproj.additional_settings.cors import *

# es-common settings
from myproj.additional_settings.es_common import *

# djangorestframework
from myproj.additional_settings.drf import *