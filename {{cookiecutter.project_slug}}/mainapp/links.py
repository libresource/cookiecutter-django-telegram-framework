from telegram_framework import links
from . import actions


bot_links = [
    links.on_command(actions.introduction, 'start', 'run bot'),
]
