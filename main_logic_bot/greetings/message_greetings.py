from aiogram import Router, types as tp, F
from aiogram.filters import CommandStart
from main_logic_bot.greetings import kb_greetings as kb
from utils.loader_token import Token

router = Router(name='message_greetings')


@router.message(CommandStart(), F.chat.type == 'private')
async def start_handler(message: tp.Message) -> None:
    """Функция по обработке команды /start"""

    if str(message.from_user.id) not in [Token(key='ADMIN_ID').find(), Token(key='MY_ID').find()]:
        return
    
    text = f'''
Привет, <b>{message.from_user.full_name}</b> 👋
Добавь меня в свой чат 💬
'''

    await message.answer(
        text=text,
        reply_markup=kb.inline.start_link
    )
