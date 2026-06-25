"""
Most Django settings configured here, with some modules in /modules
"""

import os

# load environment from file
import environ
env = environ.Env(
    DEBUG=(bool, False) # set casting, default value
)
environ.Env.read_env()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', False)

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
]

CORS_ORIGIN_WHITELIST = []

if DEBUG:
    CORS_ORIGIN_WHITELIST.append('http://localhost:3000')

# if using render to deploy, it will automatically inject this env var
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
   ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# add render frontend to allowed cors list
RENDER_FRONTEND_SERVICE = os.environ.get('RENDER_FRONTEND_SERVICE')
if RENDER_FRONTEND_SERVICE:
   CORS_ORIGIN_WHITELIST.append("https://%s.onrender.com" % RENDER_FRONTEND_SERVICE)


# Application definition

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # installed apps
    'corsheaders',
    'rest_framework',

    # our apps
    'api',
    'app',
    'test_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_HOST_PORT'],
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# django logging config
ROOT_LOG_LEVEL = os.environ.get('ROOT_LOG_LEVEL', 'INFO')
DJANGO_LOG_LEVEL = os.environ.get('DJANGO_LOG_LEVEL', 'INFO')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'simple': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'verbose': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[{name}] {levelname} {asctime} {module}:{lineno} {funcName}() {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{name}] {levelname} {message}',
            'style': '{',
        },
    },
    'root': {
        'handlers': ['simple'],
        'level': ROOT_LOG_LEVEL,
        'propagate': False,
    },
    'loggers': {
        'django': {
            'handlers': ['simple'],
            'level': DJANGO_LOG_LEVEL,
            'propagate': True,
        },
        'django.request': {
            'level': DJANGO_LOG_LEVEL,
            'handlers': ['verbose'],
            'propagate': False,
        },
        'gunicorn' : {
            'level': DJANGO_LOG_LEVEL,
            'handlers': ['verbose'],
            'propagate': False,
        },
        'app': {  # custom app logger
            'handlers': ['simple'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# django rest framework
# API endpoints are open (AllowAny) — no authentication required.
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
