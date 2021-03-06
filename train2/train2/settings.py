"""
Django settings for train2 project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import tempfile

BASE_URL = 'http://otrain.org'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ei1vd+bsrw(vf!-c(8h_t^z%jm0k)&l!2s21cl8tl=pou0nq^g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'data',
    'xlparser',
    'ui',
    'info',
    'browse',
    'rest_framework_swagger',
    'corsheaders'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',  # cache - eran
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',  # cache - eran
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'train2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'train2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'train2',
        'USER': 'train2',
        'PASSWORD': 'somepassword',
        'HOST': 'localhost',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'he'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TMP_ROOT = tempfile.gettempdir()


def find_ot_log_dir():
    ot_log_dir = '/var/log/opentrain'
    ot_log_dir2 = os.path.join(TMP_ROOT, 'opentrain_logs')
    try:
        if not os.path.exists(ot_log_dir):
            os.makedirs(ot_log_dir)
        return ot_log_dir
    except (OSError, IOError) as e:
        # print('>>> Failed to create {0}: {1} - falling back to {2}'.format(ot_log_dir,
        #                                                                    e,
        #                                                                    ot_log_dir2))
        if not os.path.exists(ot_log_dir2):
            os.makedirs(ot_log_dir2)
    return ot_log_dir2


OT_LOG_DIR = find_ot_log_dir()

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(TMP_ROOT, 'opentrain_cache'),
        'TIMEOUT': 1 * 24 * 60 * 0  # one day
    }
}

NO_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass

try:
    from local_settings import *
except ImportError:
    pass

if NO_CACHE:
    MIDDLEWARE_CLASSES.remove('django.middleware.cache.UpdateCacheMiddleware')
    MIDDLEWARE_CLASSES.remove('django.middleware.cache.FetchFromCacheMiddleware')

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': "==========================================\n[%(asctime)s %(levelname)s] %(message)s"
        },
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(module)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%m/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(OT_LOG_DIR, 'error.log'),
            'formatter': 'simple',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'errors': {
            'handlers': ['file'],
        },
    },
}
