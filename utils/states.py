from aiogram.fsm.state import State, StatesGroup


class BadWordState(StatesGroup):
    """Класс для state плохих слов"""

    bad_word_add = State()
    bad_word_remove = State()
