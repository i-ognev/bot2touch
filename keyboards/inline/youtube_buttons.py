from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.youtube_callback import youtube_call

keyboard_youtube = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="✔ У меня есть канал",
                                                    callback_data=youtube_call.new(item_name="есть_канал")
                                                ),
                                                InlineKeyboardButton(
                                                    text="❌ У меня нет канала",
                                                    callback_data=youtube_call.new(item_name="нет_канала")
                                                )
                                            ],
                                        ])
