from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить в чат ⬇️', url='https://t.me/usernames_bot_user_bot?startgroup=start')
        ]
    ]
)
