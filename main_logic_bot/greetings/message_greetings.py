import os

from aiogram import Router, types as tp, F
from aiogram.filters import CommandStart
from main_logic_bot.greetings import kb_greetings as kb
from data.loader_file import load_file

router = Router(name='message_greetings')


@router.message(CommandStart(), F.chat.type == 'private')
async def start_handler(message: tp.Message) -> None:
    """Функция по обработке команды /start"""

    text = f'''
Привет, <b>{message.from_user.full_name}</b> 👋
Добавь меня в свой чат 💬
'''

    await message.answer(
        text=text,
        reply_markup=kb.inline.start_link
    )


# @router.message()
# async def echo(message: tp.Message) -> None:
#     """Функция по сохранению фотографий"""

#     # if not message.photo:
#     #     await message.answer(text='Нет фотки, кыш!')
#     #     return

#     # await message.answer(text='О, фотка')

#     # file_info = await message.bot.get_file(message.photo[-1].file_id)
#     # download_path = os.path.join('data/photo', file_info.file_path.split('/')[-1])

#     # await message.bot.download_file(
#     #     file_path=file_info.file_path,
#     #     destination=download_path
#     # )

#     link = 'https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%82%D1%80%D0%B0%D0%B3%D0%B8%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%BE%D0%B0%D0%BB%D1%8E%D0%BC%D0%B8%D0%BD%D0%B0%D1%82_%D0%BD%D0%B0%D1%82%D1%80%D0%B8%D1%8F'
#     text = f'''
# <b>Лера</b> хочет данный товар!

# <blockquote><b><a href='{link}'>Ссылка на товар 🔗</a></b></blockquote>
# '''

#     await message.answer(
#         text=text
#     )