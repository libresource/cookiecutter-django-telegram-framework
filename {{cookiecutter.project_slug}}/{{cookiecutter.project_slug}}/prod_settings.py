from .base_settings import *  # pylint: disable=wildcard-import,unused-wildcard-import

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = []

LOCAL_HOSTS = {'127.0.0.1', 'localhost'}
SERVER_IP = os.getenv('SERVER_IP', '127.0.0.1')
SERVER_DOMAIN = os.getenv('SERVER_DOMAIN', 'example.com')

LOCAL_HOSTS.add(SERVER_IP)

for host in LOCAL_HOSTS:
    ALLOWED_HOSTS.append(host)

# ADMIN SETTINGS
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')

# Telegram Bot Settings
TELEGRAM_BOT_TYPE = 'pyTelegramBotAPI'
