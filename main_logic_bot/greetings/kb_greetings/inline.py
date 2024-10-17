from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить в чат ⬇️', url='https://t.me/TestOxideBot?startgroup=start')
        ]
    ]
)
