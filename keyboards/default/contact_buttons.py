from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_contacts = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оставить номер телефона",
                           request_contact=True)
        ]
    ],
    resize_keyboard=True
)