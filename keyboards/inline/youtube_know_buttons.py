from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yotube_know_callback import youtube_know_call

keyboard_know_youtube = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text="✔ Знаю что делать",
                                                         callback_data=youtube_know_call.new(
                                                             item_name="знаю")
                                                     ),
                                                     InlineKeyboardButton(
                                                         text="❌ Не знаю что делать",
                                                         callback_data=youtube_know_call.new(
                                                             item_name="не_знаю(с каналом)")
                                                     )
                                                 ],
                                             ])
