import logging

from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.choice_buttons import pear_keyboard
from keyboards.inline.data_buttons import keyboard_dat
from loader import dp


@dp.message_handler(Text(contains="Нужнаавпывап"))
async def get_cons(message: types.Message):
    await message.answer("Вы можете связаться с нами самостоятельно:\n\n"
                         "🔹 Позвонить нам по телефону  8 922 633 40 16\n\n"
                         "🔹 Написать нам на почту  info@2touch.ru\n\n"
                         "🔹 Или можете оставить свои данные и мы свяжемся с вами\n\n",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer("Желаете оставить свои данные?", reply_markup=keyboard_dat)


@dp.callback_query_handler(text_contains="желаю")
async def get_cons2(call: CallbackQuery):
    await call.answer(cache_time=60)

    call_data = call.data

    logging.info(f"{call_data=}")

    await call.message.answer("Выбрали желаю",
                              reply_markup=pear_keyboard)
    await call.message.edit_reply_markup()
