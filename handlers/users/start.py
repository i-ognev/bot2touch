from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_photo("https://ladyle.ru/images/ladyle/2020/04/ddvn-sfxkaa_p4t.jpg",
                               "👋👋👋 Приветствуем вас в нашем телеграмм-боте 2touch. "
                               "Здесь мы поможем вам составить заявку для обращения к нашим услугам.\n\n"
                               "Для начала давайте познакомимся!\n\n"
                               "Как к вам обращаться? ⤵")


