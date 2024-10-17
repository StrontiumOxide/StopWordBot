from aiogram import Router, types as tp, F
from aiogram.filters import Command
from main_logic_bot.change_bad_words import kb_change_bad_words as kb
from utils.loader_token import Token

router = Router(name='message_change_bad_words')


@router.message(Command(commands=['change_bad_words']), F.chat.type == 'private')
async def start_handler(message: tp.Message) -> None:
    """Функция по обработке команды /change_bad_words"""

    # if str(message.from_user.id) not in [Token(key='ADMIN_ID').find(), Token(key='MY_ID').find()]:
    #     return

    text = f'''
<b>Панель администратора</b> ⚒️
Что вы хотите сделать со словами?
'''

    await message.answer(
        text=text,
        reply_markup=kb.inline.change_words
    )
