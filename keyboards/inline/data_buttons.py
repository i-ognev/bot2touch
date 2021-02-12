from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.data_callback import data_call

keyboard_data = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(
                                                 text="Желаю",
                                                 callback_data=data_call.new(item_name="желаю")
                                             ),
                                             InlineKeyboardButton(
                                                 text="Не желаю",
                                                 callback_data=data_call.new(item_name="не_желаю")
                                             )
                                         ]
                                     ])

site_keyboard = InlineKeyboardMarkup()

SITE_LINK = "https://yandex.ru/"

site_link = InlineKeyboardButton(text="Перейти на сайт", url=SITE_LINK)
