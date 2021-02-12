import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_menu import keyboard_menu
from loader import dp
from states.name_client import NameClient


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_photo("https://ladyle.ru/images/ladyle/2020/04/ddvn-sfxkaa_p4t.jpg",
                               "👋👋👋 Приветствуем вас в нашем телеграмм-боте 2touch. "
                               "Здесь мы поможем вам составить заявку для обращения к нашим услугам.\n\n"
                               "Для начала давайте познакомимся!\n\n"
                               "Как к вам обращаться? ⤵")

    await NameClient.next()


@dp.message_handler(state=NameClient.NC)
async def answer_nc(message: types.Message, state: FSMContext):
    answer = message.text
    logging.info = f"Psfdgfsd ={answer}"
    await message.answer(f"🤝🤝🤝 Очень рады знакомству с Вами {answer}!")
    await state.finish()
    await message.answer("Что вас интересует?", reply_markup=keyboard_menu)
