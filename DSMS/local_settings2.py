from .settings import *

SECRET_KEY = 'j*dz()3@h$o6@f*&ipn7$-%n&u54hh7gbe7!$d+loib-)*qo1*'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'SMS',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SITE_ID = 2