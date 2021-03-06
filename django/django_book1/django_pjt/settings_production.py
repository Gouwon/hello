import os
import sys
import json
from .settings import *

# if(os.environ.get('MYSQL_ROOT_HOST', None) == None):
#     os.system('source ~/workspace/hello/django/export.sh')
#     print('\n\n\n os.environ >>>>> ', os.environ)

data = json_data['production']

import pprint
pprint(data)

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'HOST': os.environ['MYSQL_ROOT_HOST'],
        # 'NAME': os.environ['MYSQL_DATABASE'],
        # 'USER': os.environ['MYSQL_USER'],
        # 'PASSWORD': os.environ['MYSQL_ROOT_PASSWORD'],
        'HOST': data['MYSQL_ROOT_HOST'],
        'NAME': data['MYSQL_DATABASE'],
        'USER': data['MYSQL_USER'],
        'PASSWORD': data['MYSQL_ROOT_PASSWORD'],
        'PORT': 3306,
        'TEST': {
            'NAME': 'test_dooodb',
            'OPTIONS': {
                'charset': 'utf8',
            }
        },
    }
}

# django superuser stroed in this db using --settings=django_pjt.settings_production
## check this site for more information about superuser
# https://swarf00.github.io/2018/12/07/registration.html