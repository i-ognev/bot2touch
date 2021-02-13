from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.beer_type_callback import beer_type_call

keyboard_type_beer = InlineKeyboardMarkup(row_width=2,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(
                                                      text="✔️ Темное",
                                                      callback_data=beer_type_call.new(item_name="темное")
                                                  ),
                                                  InlineKeyboardButton(
                                                      text="✔️ Светлое",
                                                      callback_data=beer_type_call.new(item_name="светлое")
                                                  )
                                              ],
                                          ])
