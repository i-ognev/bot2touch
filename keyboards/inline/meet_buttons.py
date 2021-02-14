from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.meet_callback import meet_call

keyboard_meet = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(
                                                 text="🍻 По пиву",
                                                 callback_data=meet_call.new(item_name="по_пиву")
                                             ),
                                             InlineKeyboardButton(
                                                 text="☕ Кофейня",
                                                 callback_data=meet_call.new(item_name="кофейня")
                                             )
                                         ],
                                     ])
