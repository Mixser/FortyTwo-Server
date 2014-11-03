from base import INSTALLED_APPS


DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

CURRENT_HOST = "dry-oasis-8791.herokuapp.com"
BASE_URL = "http://" + CURRENT_HOST

# Email sending (Mandrill App)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
# EMAIL_HOST_USER = 'gleb@razortheory.com'
# EMAIL_HOST_PASSWORD = 'UahI2QbplH25AxQeqt6oJQ'

DEFAULT_FROM_EMAIL = 'noreply@%s' % CURRENT_HOST
SERVER_EMAIL = DEFAULT_FROM_EMAIL

########## S3 CONFIGURATION
INSTALLED_APPS += (
    'storages',
)

AWS_STORAGE_BUCKET_NAME = 'xxxxxx'
AWS_ACCESS_KEY_ID = 'xxxxxx'
AWS_SECRET_ACCESS_KEY = 'xxxxxx'

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL + 'static/'
MEDIA_URL = S3_URL + 'media/'

DEFAULT_FILE_STORAGE = 'fortytwo.settings.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'fortytwo.settings.s3utils.StaticRootS3BotoStorage'
