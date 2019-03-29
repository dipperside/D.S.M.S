# comment
from .settings import *

SECRET_KEY = 'ddfdrrt545*^g*&76r*kgyt7B8f^5e64d9y&()HJ0yu97T&%%7t'

DEBUG = True

# next 3 settings need to DebugToolbar
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

THUMBNAIL_DEBUG = True

# The Debug Toolbar is shown only if your IP is listed in the INTERNAL_IPS setting.
INTERNAL_IPS = ["127.0.0.1", "0.0.0.1"]

# define your databases here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SITE_ID = 1
