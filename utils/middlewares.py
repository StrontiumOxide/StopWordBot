from asyncio import sleep as asleep
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Update, Message
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from utils.config import limit_request, max_requests, bad_words


class CountMiddleware(BaseMiddleware):
    """Middleware по счёту апдейтов"""

    async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], event: Update, data: Dict[str, Any]) -> Any:
        
        if event.message:
            user_id = event.message.from_user.id
            username = event.message.from_user.full_name
        elif event.callback_query:
            user_id = event.callback_query.from_user.id
            username = event.callback_query.from_user.full_name
        else:
            return

        if user_id in limit_request:
            limit_request[user_id]['count'] += 1
        else:
            limit_request[user_id] = {'count': 1, 'status': True}

            # Выполнение соответствующего хендлера
        if limit_request[user_id]['count'] > max_requests:
            if limit_request[user_id]['status']:
                limit_request[user_id]['status'] = False
                text = f'''
⚠️ <b>ВНИМАНИЕ</b> ⚠️

<b>от API Telegram</b>
<blockquote>Уважаемый, <b>{username}</b>❗️
Вы превысили лимит по запросам 💭
Повторите пожалуйста позже ⏳
</blockquote>
'''
                if event.message:
                    await event.message.answer(
                        text=text
                    )
                else:
                    await event.callback_query.message.answer(
                        text=text
                    )
            return
        
        await handler(event, data)


class StopWordGroupMiddleware(BaseMiddleware):
    """Middleware по удалению запрещенных слов в группах"""

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], message: Message, data: Dict[str, Any]) -> Any:

        if message.chat.type not in ['group', 'supergroup']:
            await handler(message, data)
            return

        if not message.text:
            return
        
        message_text = message.text.strip().lower()

        for bad_word in bad_words:
            if bad_word in message_text:
                # await message.delete()

                # try:
                #     await message.bot.send_message(
                #         chat_id=message.from_user.id,
                #         text=f'<i>{message.from_user.full_name}</i>, Вас поймали на спаме в чужом чате!\nВы использовали запрещенное слово: <b>"{bad_word}"</b>'
                #     )
                # except (TelegramBadRequest, TelegramForbiddenError):
                #     pass
                # finally:
                #     return
                await message.answer(
                    text=f'<i>{message.from_user.full_name}</i>, Вас поймали на спаме в чужом чате ❌\nВы использовали запрещенное слово: <b>"{bad_word}"</b> 🤬'
                )
                return
        else:
            await message.reply(
                text='Одобраю ✅'
            )

        await handler(message, data)
