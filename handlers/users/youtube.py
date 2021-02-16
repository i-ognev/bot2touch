from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.yotube_problem_buttons import keyboard_problem_youtube
from keyboards.inline.youtube_buttons import keyboard_youtube
from loader import dp
from states.name_youtube import NameYuotube


@dp.callback_query_handler(text_endswith="tube")
async def get_youtube(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_youtube = call.data
    print(f"{call_youtube}")
    await call.message.answer("Имеете ли Вы канал на Youtube❓",
                              reply_markup=keyboard_youtube)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text_endswith="ть_канал")
async def get_youtube2(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_youtube2 = call.data
    print(f"{call_youtube2}")
    await call.message.answer("Какая проблема на вашем канале❓",
                              reply_markup=keyboard_problem_youtube)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text_endswith="ое(youtube)")
async def get_youtube3(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_youtube3 = call.data
    print(f"{call_youtube3}")
    await call.message.answer("☕️ Введите свой вариант ⤵")
    await NameYuotube.next()


@dp.message_handler(state=NameYuotube.YTB)
async def get_meet3(message: types.Message, state: FSMContext):
    prsite = message.text
    print(f"Свой вариант (продв):{prsite}")
    await message.answer(f"Ваш выбор: {prsite}!")
    await state.finish()
    await message.answer("Пожалуйста, оставьте свой 📞 номер телефона,"
                         " чтобы мы могли позвонить вам и назначить встречу ⤵",
                         reply_markup=keyboard_contacts)
