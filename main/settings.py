"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import datetime
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-mh^y2jkcs4f)n+!d3*li^i+1l^@@bgvdtrr9k=saqz@pt@qi4_'

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    # 'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "rest_framework_simplejwt.token_blacklist", 
    'drf_yasg',
    "custom_trip",
    "exploreapp",
    "upcoming_treks",
    "package",
    "shop",
    "review",
    "corsheaders", 
    'storages' 
   
    # 'app.entries',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",

]

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'
# ASGI_APPLICATION = 'main.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


sql_mode='STRICT_TRANS_TABLES';
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "happyhills",
        "USER": "admin",
        "HOST": 'happyhills.c2ince2oewy3.us-east-1.rds.amazonaws.com',
        "PASSWORD": 'Chandelsaurav817',
        "PORT": '3306',
      
    }
}

# import dj_database_url
# db_from_env=dj_database_url.config(conn_max_age=600)
# # DATABASES['default']=dj_database_url.config(default='postgres://xkxqixwxttrumy:64b2e0c73330e789828266dc3d7d30a0292fa77e9f5eee0bfc56c5cf840c3f33@ec2-44-194-113-156.compute-1.amazonaws.com:5432/dfhtoccch55lfv')
# DATABASES['default'].update(db_from_env)




REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    # Parser classes priority-wise for Swagger
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.JSONParser",
    ],
    # "EXCEPTION_HANDLER": "app.util.permission_error_handler",
}

SWAGGER_SETTINGS = {
    "DOC_EXPANSION": "none",
    "TAGS_SORTER": "alpha",
    "OPERATIONS_SORTER": "alpha",
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": datetime.timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": datetime.timedelta(days=1),
}



AUTH_USER_MODEL='exploreapp.User'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# SERVE_FROM_S3 = True

if not DEBUG:
    print("________1_______")
    from main.aws.conf import *

    # STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
    # MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")
    # STATIC_URL = "/static_url/"
    # MEDIA_URL = "/media_url/"
    # STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)

else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")
    STATIC_URL = "/static_url/"
    MEDIA_URL = "/media_url/"
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_cdn"),)


    # STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)
    # AWS_ACCESS_KEY_ID = "AKIA2K5WZGM5LPVKVIKY"
    # AWS_SECRET_ACCESS_KEY = "biovwSYM8PUJPK1IqkOdpWZHZy3VzQUIFezO7LM"
    # AWS_S3_REGION_NAME = "us-east-1"  # e.g. us-east-2
    # AWS_STORAGE_BUCKET_NAME = "happyhills-s3"
    # AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    # # AWS_S3_CUSTOM_DOMAIN = "d2dr6wwncpi0to.cloudfront.net"
    # AWS_S3_OBJECT_PARAMETERS = {
    #     "CacheControl": "max-age=86400",
    # }
    # AWS_LOCATION = "static"

    # STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    # STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    # DEFAULT_FILE_STORAGE = "main.storage_backends.MediaStorage"
AWS_STORAGE_BUCKET_NAME = "happyhills-s3bucket"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATIC_ROOT =BASE_DIR / 'static'
# STATIC_URL = '/static/'


# STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
# MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")
# STATIC_URL = "/static_url/"
# MEDIA_URL = "/media_url/"


# STATICFILES_DIRS = [
#                     os.path.join(BASE_DIR, 'static')
#                ]

# if DEBUG:
#         STATICFILES_DIRS = [
#                     os.path.join(BASE_DIR, 'static')
#                ]
# else:
#         STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER ="chandelsaurav0817@gmail.com" #config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD ="********"  #config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:3000",
# ]   


CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
# "https://medical.softuvo.xyz",
# "http://medical.softuvo.xyz",
# "https://medicalapi.softuvo.xyz",
# "http://medicalapi.softuvo.xyz",
"http://localhost:3000",
"http://127.0.0.1:3000",
# "http://127.0.0.1:8000",
# "http://192.168.1.221:8000",
]


CORS_ALLOW_ALL_ORIGINS = True
# CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOW_METHODS = [
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# ]

# CORS_ALLOW_HEADERS = [
#     "accept",
#     "accept-encoding",
#     "authorization",
#     "content-type",
#     "dnt",
#     "origin",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
# ]




#while deploy on aws 

###sudo nano /etc/systemd/system/gunicorn.socket 
# [Unit]
# Description=gunicorn socket

# [Socket]
# ListenStream=/run/gunicorn.sock

# [Install]
# WantedBy=sockets.target


###sudo nano /etc/systemd/system/gunicorn.service
# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/project/happyhills-aws
# ExecStart=/home/ubuntu/project/env/bin/gunicorn \
#          --access-logfile - \
#          --workers 3 \
#          --bind unix:/run/gunicorn.sock \
#          main.wsgi:application

# [Install]
# WantedBy=multi-user.target

# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/project/clg-final-project-eshop
# ExecStart=/home/ubuntu/project/env/bin/gunicorn \
#          --access-logfile - \
#          --workers 3 \
#          --bind unix:/run/gunicorn.sock \
#          main.wsgi:application

# [Install]
# WantedBy=multi-user.target