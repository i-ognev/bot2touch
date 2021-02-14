from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.default.contact_buttons import keyboard_contacts
from keyboards.inline.meet_buttons import keyboard_meet
from keyboards.inline.meet_coffee_buttons import keyboard_coffee
from loader import dp
from states.name_coffee import NameCoffee


@dp.message_handler(Text(endswith="стречу"))
async def get_meet(message: types.Message):
    call_meet = message.text
    print(f"Какой напиток?:{call_meet}")
    await message.answer("👍 Давайте теперь определимся с напитками",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer("Предпочитаете ☕ Кофе или 🍻 по Пиву❓",
                         reply_markup=keyboard_meet)


# @dp.callback_query_handler(text_contains="кофейня")
# async def get_meet2(call: CallbackQuery):
#    await call.answer(cache_time=60)
#    call_meet2 = call.data
#    print(f"Что пить?:{call_meet2}")
#    await call.message.answer("👍 Давайте теперь определимся с напитками", )
#    await call.message.answer("Предпочитаете ☕ Кофе или 🍻 по Пиву❓",
#                              reply_markup=keyboard_meet)
#    await call.message.edit_reply_markup()


@dp.callback_query_handler(text_endswith="ня")
async def get_meet3(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_meet3 = call.data
    print(f"Где встреча?:{call_meet3}")
    await call.message.answer("👍 Давайте теперь определимся с кофейней")
    await call.message.answer("Какую кофейню предпочитаете❓",
                              reply_markup=keyboard_coffee)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text_endswith="ант")
async def get_meet2(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_meet4 = call.data
    print(f"Где встреча?:{call_meet4}")
    await call.message.answer("☕️ Введите название кофейни ⤵")
    await NameCoffee.next()


@dp.message_handler(state=NameCoffee.Cof)
async def get_meet3(message: types.Message, state: FSMContext):
    coffee = message.text
    print(f"Название кофейню:{coffee}")
    await message.answer(f"Ваш выбор: {coffee}!")
    await state.finish()
    await message.answer("Пожалуйста, оставьте свой 📞 номер телефона,"
                         " чтобы мы могли позвонить вам и назначить встречу ⤵",
                         reply_markup=keyboard_contacts)



