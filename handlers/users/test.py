import logging

from aiogram.types import CallbackQuery

from keyboards.inline.choice_buttons import pear_keyboard
from loader import dp


@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    call_data = call.data

    logging.info(f"{call_data=}")

    await call.message.answer("Выбрали желаю",
                              reply_markup=pear_keyboard)

