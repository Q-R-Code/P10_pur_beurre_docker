from . import *

SECRET_KEY = 'v=^p*!*ackpa8nx@=i-+t$!kp22r5rtz7ynx8h*9$b39#iq8s6'

DEBUG = False

ALLOWED_HOSTS = ['192.168.1.49']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '192.168.1.49',
        'PORT': '5432',
    }
}
