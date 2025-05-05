from .base_settings import *  # pylint: disable=wildcard-import,unused-wildcard-import

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

TELEGRAM_BOT_TYPE = 'Dummy'
