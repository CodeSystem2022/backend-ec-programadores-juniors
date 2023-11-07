import os
from .settings import * 
from .settings import BASE_DIR


ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGIN = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATIC_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR,'staticFiles')

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']

parameters= {pair.split('='):pair.split('=')[1] for pair in connection_string.split('')}

DATABASES = {
    'default':{
        'ENGINE':'django.db.backend.postgresql',
        'NAME':parameters['dbname'],
        'HOST':parameters['host'],
        'USER':parameters['user'],
        'PASSWORD':parameters['password']
    }
}