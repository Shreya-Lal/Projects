

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogpost.settings')

application = Cling(get_wsgi_application())

if os.getcwd() == '/app':
    from whitenoise.django import DjangoWhiteNoise
    application =  DjangoWhiteNoise(application)
