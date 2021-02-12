from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import buy_callback

# Вариант 1, как в прошлом уроке
choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text="Купить грушу",
                                                           callback_data=buy_callback.new(item_name="pear")),
                                      InlineKeyboardButton(text="Купить яблоки",
                                                           callback_data=buy_callback.new(item_name="apple"))
                                  ],
                                  [
                                      InlineKeyboardButton(text="Отмена", callback_data="next")
                                  ]
                              ])

# Вариант 2 - с помощью row_width и insert.
# choice = InlineKeyboardMarkup(row_width=2)

# buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="груш"))
# choice.insert(buy_pear)

# buy_apples = InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:5")
# choice.insert(buy_apples)

# cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
# choice.insert(cancel_button)

URL_APPLES = "https://yandex.ru/"

URL_PEAR = "https://yandex.ru/"
# А теперь клавиатуры со ссылками на товары
pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url=URL_APPLES)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url=URL_PEAR)
    ]
])
