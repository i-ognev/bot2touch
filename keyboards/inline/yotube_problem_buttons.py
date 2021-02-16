from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yotube_problem_callback import youtube_problem_call

keyboard_problem_youtube = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text="📽 Самостоятельно занимались каналом",
                                                            callback_data=youtube_problem_call.new(
                                                                item_name="занимались_самост")
                                                        )
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            text="📽 Ранее продвигался",
                                                            callback_data=youtube_problem_call.new(
                                                                item_name="ранее_подвиг")
                                                        ),
                                                        InlineKeyboardButton(
                                                            text="📽 Другое",
                                                            callback_data=youtube_problem_call.new(
                                                                item_name="другое(youtube)")
                                                        )
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            text="📽 Нет контента",
                                                            callback_data=youtube_problem_call.new(
                                                                item_name="нет_контента")
                                                        )
                                                    ]
                                                ])
