from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.beer_place_callback import beer_place_call

keyboard_place_beer = InlineKeyboardMarkup(row_width=2,
                                           inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(
                                                       text="🍻 В баре",
                                                       callback_data=beer_place_call.new(item_name="в_баре")
                                                   ),
                                                   InlineKeyboardButton(
                                                       text="💼 В офисе",
                                                       callback_data=beer_place_call.new(item_name="в_офисе")
                                                   )
                                               ]
                                           ])
