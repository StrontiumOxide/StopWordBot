from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllChatAdministrators, BotCommandScopeDefault
from utils.loader_token import Token


async def set_commands(bot: Bot) -> None:
    """Данная функция добавляет меню в бота с командами ниже"""

    commands_private = [
        BotCommand(
            command="start",
            description="Запуск бота ▶️"
        ),
        BotCommand(
            command='change_bad_words',
            description='Изменить список запрещённых слов ⚒️'
        )
    ]

    await bot.set_my_commands(commands=commands_private, scope=BotCommandScopeDefault())

    command_group = [
        BotCommand(
            command="ban",
            description="Забанить ❌"
        ),
        BotCommand(
            command='unban',
            description='Разбанить ✅'
        )
    ]

    await bot.set_my_commands(commands=command_group, scope=BotCommandScopeAllChatAdministrators())
