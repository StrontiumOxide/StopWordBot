from aiogram import Router, types as tp
from aiogram.filters import Command
from utils.loader_token import Token

router = Router(name='message_banning')


@router.message(Command(commands=['ban']))
async def ban_handler(message: tp.Message) -> None:
    """Функция по обработке команды /ban"""

        # Проверка на группу/супергруппу
    if message.chat.type not in ['group', 'supergroup']:
        return
    
        # Проверка на чужых
    if str(message.from_user.id) not in [Token(key='ADMIN_ID').find(), Token(key='MY_ID').find()]:
        return
    
    if not message.reply_to_message:
        return
    
    if str(message.reply_to_message.from_user.id) not in [Token(key='ADMIN_ID').find(), Token(key='MY_ID').find()]:
        try:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
        except Exception:
            pass


@router.message(Command(commands=['unban']))
async def ban_handler(message: tp.Message) -> None:
    """Функция по обработке команды /unban"""

        # Проверка на группу/супергруппу
    if message.chat.type not in ['group', 'supergroup']:
        return
    
        # Проверка на чужых
    if str(message.from_user.id) not in [Token(key='ADMIN_ID').find(), Token(key='MY_ID').find()]:
        return
    
    if not message.reply_to_message:
        return

    if str(message.reply_to_message.from_user.id) not in [Token(key='ADMIN_ID').find(), Token(key='MY_ID').find()]:
        try:
            await message.bot.unban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
        except Exception:
            pass
