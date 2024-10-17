from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from utils.config import bad_words

remove = ReplyKeyboardRemove()

list_words_kb = ReplyKeyboardMarkup(
    keyboard=[[*map(lambda word: KeyboardButton(text=word), sorted(bad_words))]],
    resize_keyboard=True
)

def create_list_words_kb() -> ReplyKeyboardMarkup:
    """Функция создаёт клавиатуру с кнопками в виде плохих слов"""

    kb = ReplyKeyboardBuilder()
    kb.row(*map(lambda word: KeyboardButton(text=word), sorted(bad_words)), width=1)
    kb = kb.as_markup()
    kb.resize_keyboard = True
    return kb
