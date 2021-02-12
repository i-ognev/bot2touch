from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нужна консультация")
        ],
        [
            KeyboardButton(text="хочу встретиться")
        ],
        [
            KeyboardButton(text="стать клиентом")
        ],
        [
            KeyboardButton(text="обсудить за пивом")
        ]
    ],
    resize_keyboard=True
)
