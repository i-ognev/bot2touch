from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.beer_marka_callback import beer_marka_call

keyboard_marka_beer = InlineKeyboardMarkup(row_width=2,
                                           inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(
                                                      text="✔️ Tsingtao",
                                                      callback_data=beer_marka_call.new(item_name="tsingtao")
                                                  ),
                                                  InlineKeyboardButton(
                                                      text="✔️ Steen Brugge",
                                                      callback_data=beer_marka_call.new(item_name="steen_brugge")
                                                  )
                                              ],
                                              [
                                                  InlineKeyboardButton(
                                                      text="✔️ Corsendonk Blanche",
                                                      callback_data=beer_marka_call.new(item_name="corsendonk_blanche")
                                                  )
                                              ]
                                          ])
