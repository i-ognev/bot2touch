from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.data_callback import dat_call

keyboard_dat = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="✔ Желаю",
                                                callback_data=dat_call.new(item_name="желаю")
                                            ),
                                            InlineKeyboardButton(
                                                text="❌ Не желаю",
                                                callback_data=dat_call.new(item_name="не_желаю")
                                            )
                                        ]
                                    ])

SITE_LINK = "https://yandex.ru/"

site_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="➡ Перейти на сайт", url=SITE_LINK)
    ]
])
