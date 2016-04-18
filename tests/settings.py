# Put in local_settings.py so you can exclude from upload.
# example: '/home/[username]/google-cloud-sdk/platform/google_appengine'
GAE_PATH = None

try:
    from local_settings import *
except ImportError:
    pass
