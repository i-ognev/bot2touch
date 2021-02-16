from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.client_smm_callback import client_smm_call

keyboard_smm_client = InlineKeyboardMarkup(row_width=2,
                                           inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(
                                                       text="🔷 Есть стратегия развития",
                                                       callback_data=client_smm_call.new(item_name="Есть_стр")
                                                   ),
                                                   InlineKeyboardButton(
                                                       text="🔶 Нет стратегии развития",
                                                       callback_data=client_smm_call.new(item_name="Нет_стр")
                                                   )
                                               ],
                                           ])
