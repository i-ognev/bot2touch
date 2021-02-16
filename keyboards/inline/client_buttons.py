from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.client_callback import client_call

keyboard_client = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(
                                                   text="🎯 Нужен весь комплекс",
                                                   callback_data=client_call.new(item_name="Комплекс")
                                               ),
                                               InlineKeyboardButton(
                                                   text="📣 Интересует SMM",
                                                   callback_data=client_call.new(item_name="SMM")
                                               )
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="🎥 Поработаем с youtube",
                                                   callback_data=client_call.new(item_name="Youtube")
                                               )
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="🖥 Интересует создание сайта",
                                                   callback_data=client_call.new(item_name="Созд_сайта")
                                               )
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="⚙ Нужно продвижение сайта",
                                                   callback_data=client_call.new(item_name="Продв_сайта")
                                               )
                                           ]
                                       ])
