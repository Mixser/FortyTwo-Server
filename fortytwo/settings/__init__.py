import os

from base import *


ENV = os.environ.get('ENV', 'PROD').upper()

if ENV == 'DEV':
    from fortytwo.settings.dev import *
elif ENV == 'PROD':
    from fortytwo.settings.prod import *

