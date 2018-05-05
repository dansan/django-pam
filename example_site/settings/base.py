"""
Django settings for django_pam project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/<version>/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/<version>/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Login and redirect URLs.
LOGIN_URL = 'django-pam:login'
LOGIN_REDIRECT_URL = '/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$-ny_c64w5c3sjpjo=nzayyr7!r=pjs_bc*1(y&e@n!6bga()3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django_pam',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

ROOT_URLCONF = 'example_site.urls'

TEMPLATES = [
    {'BACKEND': 'django.template.backends.django.DjangoTemplates',
     'DIRS': [
         os.path.join(BASE_DIR, 'templates'),
         ],
     'OPTIONS': {
         'context_processors': [
             'django.template.context_processors.debug',
             'django.template.context_processors.request',
             'django.template.context_processors.static',
             'django.contrib.auth.context_processors.auth',
             'django.contrib.messages.context_processors.messages',
             ],
         'debug': DEBUG,
         'loaders': [
             'django.template.loaders.filesystem.Loader',
             'django.template.loaders.app_directories.Loader',
             ]
         },
     },
    ]

WSGI_APPLICATION = 'example_site.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': ('django.contrib.auth.password_validation.'
              'UserAttributeSimilarityValidator'),
     },
    {'NAME': ('django.contrib.auth.password_validation.'
              'MinimumLengthValidator'),
     },
    {'NAME': ('django.contrib.auth.password_validation.'
              'CommonPasswordValidator'),
     },
    {'NAME': ('django.contrib.auth.password_validation.'
              'NumericPasswordValidator'),
     },
    ]

# Django auth backends.
AUTHENTICATION_BACKENDS = [
    'django_pam.auth.backends.PAMBackend',
    'django.contrib.auth.backends.ModelBackend',
    ]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = BASE_DIR + SITE_URL + 'static/'

STATIC_URL = SITE_URL + 'static/'

# Additional locations of static files
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(BASE_DIR, 'dev')),
    )

# A sample logging configuration. The only tangible logging performed by this
# configuration is to send an email to the site admins on every HTTP 500 error
# when DEBUG=False. See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOG_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'logs'))
not os.path.isdir(LOG_DIR) and os.mkdir(LOG_DIR, 0o0775)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ("%(asctime)s %(levelname)s %(module)s %(funcName)s "
                       "[line:%(lineno)d] %(message)s")
            },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
            },
        },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            },
        },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': 'True',
            },
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
            },
        'examples_file': {
            'class': ('example_site.common.loghandlers'
                      '.DeferredRotatingFileHandler'),
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': '/dev/null',
            'maxBytes': 50000000, # 50 Meg bytes
            'backupCount': 5,
            },
        'django_pam_file': {
            'class': ('example_site.common.loghandlers'
                      '.DeferredRotatingFileHandler'),
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': '/dev/null',
            'maxBytes': 50000000, # 50 Meg bytes
            'backupCount': 5,
            },
        },
    'loggers': {
        'django.request': {
            'handlers': ['examples_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        'examples': {
            'handlers': ('examples_file', 'mail_admins',),
            'level': 'ERROR',
            'propagate': True,
            },
        'django_pam': {
            'handlers': ('django_pam_file', 'mail_admins',),
            'level': 'ERROR',
            'propagate': True,
            },
        },
    }
