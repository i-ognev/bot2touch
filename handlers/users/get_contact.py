from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.default.contact_buttons import keyboard_contacts
from loader import dp


@dp.callback_query_handler(text_contains="желаю")
@dp.callback_query_handler(text_contains="в_баре")
@dp.callback_query_handler(text_contains="темное")
@dp.callback_query_handler(text_contains="tsingtao")
@dp.callback_query_handler(text_contains="steen_brugge")
@dp.callback_query_handler(text_contains="corsendonk_blanche")
@dp.callback_query_handler(text_contains="Дело")
@dp.callback_query_handler(text_contains="Труда")
@dp.callback_query_handler(text_contains="Поль")
@dp.callback_query_handler(text_contains="Есть_стр")
@dp.callback_query_handler(text_contains="Нет_стр")
@dp.callback_query_handler(text_contains="Лендинг")
@dp.callback_query_handler(text_contains="Многостраничник")
@dp.callback_query_handler(text_contains="Интернет_магазин")
@dp.callback_query_handler(text_contains="не_знаю_точно")
@dp.callback_query_handler(text_contains="Таргет_рекл")
@dp.callback_query_handler(text_contains="ЯД")
@dp.callback_query_handler(text_contains="GA")
@dp.callback_query_handler(text_contains="Комплекс(продв)")
@dp.callback_query_handler(text_contains="Другое(продв)")
@dp.callback_query_handler(text_contains="занимались_самост")
@dp.callback_query_handler(text_contains="ранее_подвиг")
@dp.callback_query_handler(text_contains="нет_контента")
@dp.callback_query_handler(text_contains="знаю")
@dp.callback_query_handler(text_contains="не_знаю(с каналом)")
async def get_cons2(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_phone = call.data
    print(f"{call_phone}")
    await call.message.answer("Пожалуйста, оставьте свой 📞 номер телефона,"
                              " чтобы мы могли позвонить вам и назначить встречу ⤵",
                              reply_markup=keyboard_contacts)
    await call.message.edit_reply_markup()


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    print(f"Номер телефона:{contact.phone_number}")
    await message.answer(f"😉😉😉 Блгодарим Вас за обращение! Ваш номер 📞 {contact.phone_number} "
                         f"был получен и передан менеджеру\n\n"
                         "🕐🕐🕐 Мы обязательно свяжемся с вами в ближайшее время!",
                         reply_markup=ReplyKeyboardRemove())
