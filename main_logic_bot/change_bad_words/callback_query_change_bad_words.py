from aiogram import Router, types as tp, F
from aiogram.fsm.context import FSMContext
from utils.config import bad_words
from utils.states import BadWordState
from main_logic_bot.change_bad_words import kb_change_bad_words as kb

router = Router(name='callback_query_change_bad_words')


async def check_text(message: tp.Message) -> bool | None:
    """Функция по проверке наличия текста в сообщении"""

    if not message.text:
        await message.answer(text='Извините, в вашем сообщении нет текста 😒')
        return True
    

@router.callback_query(F.data == 'add_word')
async def add_words_handler(callback_query: tp.CallbackQuery, state: FSMContext) -> None:
    """ Функция по обработке data="add_word" """

    await callback_query.answer()
    await callback_query.message.answer(
        text='Хорошо, напишите слово или фразу, которая не должна фигурировать в сообщениях чата ☺️'
    )
  
    await state.set_state(BadWordState.bad_word_add)


@router.message(BadWordState.bad_word_add)
async def get_bad_word_add(message: tp.Message, state: FSMContext) -> None:
    """фунция по получении плохих слов и сохранения в списке"""

        # Проверка на наличие сообщения
    if await check_text(message=message): return

    word = message.text.lower()
    if word in bad_words:
        text='Данное слово/фраза уже есть в списке ☺️'
    else:
        bad_words.append(word)
        text=f'В список успешно добавлено новое слово: <b>"{word}"</b> 😎'

    await message.answer(
        text=text
    )
    await state.clear()


@router.callback_query(F.data == 'remove_word')
async def add_words_handler(callback_query: tp.CallbackQuery, state: FSMContext) -> None:
    """ Функция по обработке data="remove_word" """

    if not bad_words:
        await callback_query.answer(
            text='У вас нет запрещённых слов ❌',
            show_alert=True
        )
        return
    
    await callback_query.answer()
    await callback_query.message.answer(
        text='Какое слово вы хотите удалить? 🧐',
        reply_markup=kb.reply.create_list_words_kb()
    )

    await state.set_state(BadWordState.bad_word_remove)


@router.message(BadWordState.bad_word_remove)
async def get_bad_worde_remove(message: tp.Message, state: FSMContext) -> None:
    """Фунция по получении плохих слов и удаления из списка"""

        # Проверка на наличие сообщения
    if await check_text(message=message): return

    word = message.text.lower()
    if word not in bad_words:
        await message.answer(
            text='Такого слова нет в списке ❌'
        )
        return
    
    bad_words.remove(word)

    await message.answer(
        text=f'Слово <b>"{word}"</b> успешно удалено из списка ☺️',
        reply_markup=kb.reply.remove
    )

    await state.clear()
    