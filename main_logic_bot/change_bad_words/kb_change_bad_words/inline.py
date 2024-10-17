from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

change_words = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить ⬆️', callback_data='add_word'),
            InlineKeyboardButton(text='Убрать ⬇️', callback_data='remove_word')
        ]
    ]
)
