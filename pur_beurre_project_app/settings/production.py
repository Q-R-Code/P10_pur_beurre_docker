from . import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v=^p*!*ackpa8nx@=i-+t$!kp22r5rtz7ynx8h*9$b39#iq8s6'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

# ALLOWED_HOSTS = ['purbeurre-denicheur.herokuapp.com']
ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre',
        'USER': 'flynz',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
