DEBUG = True
TEMPLATE_DEBUG = True

CURRENT_HOST = "127.0.0.1:8000"
BASE_URL = "http://" + CURRENT_HOST

DEFAULT_FROM_EMAIL = "webmaster@example.com"

SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
