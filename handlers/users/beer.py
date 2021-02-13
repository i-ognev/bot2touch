from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.beer_marka_buttons import keyboard_marka_beer
from keyboards.inline.beer_place_buttons import keyboard_place_beer
from keyboards.inline.beer_type_buttons import keyboard_type_beer
from loader import dp


@dp.message_handler(Text(endswith="вом"))
async def get_beer(message: types.Message):
    call_beer = message.text
    print(f"Выбор в главном меню:{call_beer}")
    await message.answer("Давайте треперь определимся с местом встречи",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer("Где бы вы хотели обсудить свой проект❓",
                         reply_markup=keyboard_place_beer)


@dp.callback_query_handler(text_contains="в_офисе")
async def get_beer2(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_beer_type = call.data
    print(f"{call_beer_type}")
    await call.message.answer("Какое пиво предпочитаете❓", reply_markup=keyboard_type_beer)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text_contains="светлое")
async def get_beer2(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_beer_marka = call.data
    print(f"{call_beer_marka}")
    await call.message.answer("Какую марку предпочитаете❓", reply_markup=keyboard_marka_beer)
    await call.message.edit_reply_markup()
