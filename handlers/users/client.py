from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.default.contact_buttons import keyboard_contacts
from keyboards.inline.client_buttons import keyboard_client
from keyboards.inline.client_crsite_buttons import keyboard_crsite_client
from keyboards.inline.client_pr_buttons import keyboard_prsite_client
from keyboards.inline.client_smm_buttons import keyboard_smm_client
from keyboards.inline.yotube_problem_buttons import keyboard_problem_youtube
from keyboards.inline.youtube_buttons import keyboard_youtube
from keyboards.inline.youtube_know_buttons import keyboard_know_youtube
from loader import dp
from states.name_prsite import NamePRSite
from states.name_youtube import NameYuotube


@dp.message_handler(Text(endswith="нтом"))
async def get_client(message: types.Message):
    call_client = message.text
    print(f"Выбор в главном меню:{call_client}")
    await message.answer("👍 Прежде чем Вы станете нашим клиентом, давайте определимся с услугой,"
                         " которая Вас интересует",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer("Какая услуга вам интересна❓",
                         reply_markup=keyboard_client)


# Если выбирают весь комплекс
@dp.callback_query_handler(text_endswith="плекс")
async def get_client2(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_meet2 = call.data
    print(f"{call_meet2}")
    await call.message.answer("👍 Мы еще не знаем какую компанию вы представляете, но вы очень крутые! ))")
    await call.message.answer("Пожалуйста, оставьте свой 📞 номер телефона,"
                              " чтобы мы могли позвонить вам и назначить встречу ⤵",
                              reply_markup=keyboard_contacts)
    await call.message.edit_reply_markup()


# Если выбирают SMM
@dp.callback_query_handler(text_endswith="MM")
async def get_client3(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_meet3 = call.data
    print(f"{call_meet3}")
    await call.message.answer("Есть ли у вас стратегия развития❓",
                              reply_markup=keyboard_smm_client)
    await call.message.edit_reply_markup()


# Если выбирают Создание Сайта
@dp.callback_query_handler(text_endswith="озд_сайта")
async def get_client4(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_meet4 = call.data
    print(f"{call_meet4}")
    await call.message.answer("Какой сайт вам нужен❓",
                              reply_markup=keyboard_crsite_client)
    await call.message.edit_reply_markup()


# Если выбирают Продвижение Сайта
@dp.callback_query_handler(text_endswith="одв_сайта")
async def get_client5(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_meet5 = call.data
    print(f"{call_meet5}")
    await call.message.answer("Какое продвижение предпочитаете❓",
                              reply_markup=keyboard_prsite_client)
    await call.message.edit_reply_markup()


# Если выбирают Продвижение Сайта --> Свой вариант
@dp.callback_query_handler(text_endswith="ое(продв)")
async def get_meet6(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_meet6 = call.data
    print(f"{call_meet6}")
    await call.message.answer("☕️ Введите свой вариант ⤵")
    await NamePRSite.next()


@dp.message_handler(state=NamePRSite.PRS)
async def get_meet3(message: types.Message, state: FSMContext):
    prsite = message.text
    print(f"Свой вариант (продв):{prsite}")
    await message.answer(f"Ваш выбор: {prsite}!")
    await state.finish()
    await message.answer("Пожалуйста, оставьте свой 📞 номер телефона,"
                         " чтобы мы могли позвонить вам и назначить встречу ⤵",
                         reply_markup=keyboard_contacts)


# Если выбирают Youtube
@dp.callback_query_handler(text_endswith="tube")
async def get_youtube(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_youtube = call.data
    print(f"{call_youtube}")
    await call.message.answer("Имеете ли Вы канал на Youtube❓",
                              reply_markup=keyboard_youtube)
    await call.message.edit_reply_markup()


# Если выбирают Youtube --> Есть канал
@dp.callback_query_handler(text_endswith="ть_канал")
async def get_youtube2(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_youtube2 = call.data
    print(f"{call_youtube2}")
    await call.message.answer("Какая проблема на вашем канале❓",
                              reply_markup=keyboard_problem_youtube)
    await call.message.edit_reply_markup()


# Если выбираюь Youtube --> Есть канал --> Свой вариант
@dp.callback_query_handler(text_endswith="ое(youtube)")
async def get_youtube3(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_youtube3 = call.data
    print(f"{call_youtube3}")
    await call.message.answer("📽️ Введите свой вариант ⤵")
    await NameYuotube.next()


@dp.message_handler(state=NameYuotube.YTB)
async def get_youtube4(message: types.Message, state: FSMContext):
    ytb = message.text
    print(f"Свой вариант(yuotube):{ytb}")
    await message.answer(f"Ваш вариант: {ytb}!")
    await state.finish()
    await message.answer("Пожалуйста, оставьте свой 📞 номер телефона,"
                         " чтобы мы могли позвонить вам и назначить встречу ⤵",
                         reply_markup=keyboard_contacts)


# Если выбираюь Youtube --> Нет канала
@dp.callback_query_handler(text_endswith="ет_канала")
async def get_youtube5(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_youtube5 = call.data
    print(f"{call_youtube5}")
    await call.message.answer("Знаете ли Вы, что делать с каналом на Youtube❓",
                              reply_markup=keyboard_know_youtube)
    await call.message.edit_reply_markup()
