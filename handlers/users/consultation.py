from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.data_buttons import keyboard_dat, site_keyboard
from loader import dp


@dp.message_handler(Text(endswith="ция"))
async def get_cons(message: types.Message):
    call_cons = message.text
    print(f"Выбор в главном меню:{call_cons}")
    await message.answer("Вы можете связаться с нами самостоятельно:\n\n"

                         "🔹 Позвонить нам по телефону 📞 8 922 633 40 16 \n\n"

                         "🔹 Написать нам на почту ✉ info@2touch.ru \n\n"

                         "🔹 Или можете оставить свои данные и мы свяжемся с вами",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer("Желаете оставить свои данные, чтобы мы сами могли связаться с вами❓",
                         reply_markup=keyboard_dat)


@dp.callback_query_handler(text_contains="не_желаю")
async def get_cons2(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_data = call.data
    print(f"{call_data}")
    await call.message.answer("Тогда свяжитесь с нами сами:\n\n"

                              "🔹 Позвоните нам по телефону 📞 8 922 633 40 16 \n\n"

                              "🔹 Напишите нам на почту ✉ info@2touch.ru \n\n"

                              "🔹 Или перейдите на наш сайт ⤵",
                              reply_markup=site_keyboard)
    await call.message.edit_reply_markup()
