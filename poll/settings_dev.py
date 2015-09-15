# -*- coding: utf-8 -*-
from settings import *
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'poll',
        'USER': 'postgres',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True