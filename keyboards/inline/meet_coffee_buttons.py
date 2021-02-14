from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.meet_coffee_callback import meet_coffee_call

keyboard_coffee = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(
                                                   text="☕ Дело не в кофе (Советская)",
                                                   callback_data=meet_coffee_call.new(item_name="Дело_не_в_кофе(Сов)")
                                               )
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="☕ Дело не в кофе (Комсомольский)",
                                                   callback_data=meet_coffee_call.new(item_name="Дело_не_в_кофе(Ком)")
                                               )
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="☕ Кофе и книги на Труда",
                                                   callback_data=meet_coffee_call.new(item_name="Кофе_и_книги(Труда)")
                                               )
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="☕ Поль Бейкери",
                                                   callback_data=meet_coffee_call.new(item_name="Поль_Бейкери")
                                               ),
                                               InlineKeyboardButton(
                                                   text="☕ Свой вариант",
                                                   callback_data=meet_coffee_call.new(item_name="Свой_вариант")
                                               )
                                           ]
                                       ])
