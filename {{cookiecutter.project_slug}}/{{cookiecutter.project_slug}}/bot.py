from telegram_framework import links, commands


bot_links = links.include_all(
    [],
    [
        'mainapp.links',
    ]
)

bot_links += [
    links.on_command(commands.user_commands, 'commands', 'Доступные команды')
]
