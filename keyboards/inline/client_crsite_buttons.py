from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.client_crsite_callback import client_crsite_call

keyboard_crsite_client = InlineKeyboardMarkup(row_width=2,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton(
                                                          text="🔷 Лендинг",
                                                          callback_data=client_crsite_call.new(item_name="Лендинг")
                                                      ),
                                                      InlineKeyboardButton(
                                                          text="🔶 Многостраничник",
                                                          callback_data=client_crsite_call.new(
                                                              item_name="Многостраничник")
                                                      )
                                                  ],
                                                  [
                                                      InlineKeyboardButton(
                                                          text="🔷 Интернет-магазин",
                                                          callback_data=client_crsite_call.new(
                                                              item_name="Интернет_магазин")
                                                      ),
                                                      InlineKeyboardButton(
                                                          text="🔶 Я не знаю точно",
                                                          callback_data=client_crsite_call.new(
                                                              item_name="не_знаю_точно")
                                                      )
                                                  ],
                                              ])
