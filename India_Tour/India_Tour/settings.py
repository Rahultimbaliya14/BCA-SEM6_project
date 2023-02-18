"""
Django settings for India_Tour project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
# from pymongo import MongoClient
# client = MongoClient()

# client = MongoClient('mongodb+srv://rahul:72485@cluster0.gtjd8qf.mongodb.net/?retryWrites=true&w=majority')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-62em4ma=+=0d00#aoygul$@+ibmt2o8#)n8og!$u=7e!@f64w1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'users',
    'package'
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

ROOT_URLCONF = 'India_Tour.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Tamplate'],
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

WSGI_APPLICATION = 'India_Tour.wsgi.application'






DATABASES ={

     
    #  'default': {
    #         'ENGINE': 'djongo',
    #         'NAME': 'India_tour',
    #         'ENFORCE_SCHEMA': False,
    #         'CLIENT': {
    #             'host': 'mongodb+srv://rahul:72485@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority',
    #             'username':'rahul',
    #             'password':'72485',
    #         }  
    #     }


            # 'default': {
            #     'ENGINE': 'django.db.backends.mysql',
            #     'NAME': 'india_tour',
            #     'USER': 'root',
            #     'PASSWORD': '',
            #     'HOST':'localhost',
            #     'PORT':'3306',
            # },


            'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            }
  
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL ='/static/'
STATICFILE_DIRS=BASE_DIR,'static' 


MEDIA_URL = '/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')

#Confugration For Send Mail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='zoomanagmentsystem@gmail.com'
EMAIL_HOST_PASSWORD='wcoyevknawxqadhm'
EMAIL_USE_TLS=True
# cujygscajxajblvs
# gorpyzyocxletdhp
'wcoyevknawxqadhm'