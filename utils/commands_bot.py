from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat


async def set_commands(bot: Bot) -> None:
    """Данная функция добавляет меню в бота с командами ниже"""

    commands = [
        BotCommand(
            command="start",
            description="Запуск бота ▶️"
        ),
        BotCommand(
            command='change_bad_words',
            description='Изменить список запрещённых слов ⚒️'
        )
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeChat(chat_id=1172020269))
