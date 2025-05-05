from telegram_framework import  use


introduction = use.template_action(
    'mainapp/bot/intro.html',
    {
        'name': 'demo',
    }
)
