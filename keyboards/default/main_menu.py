from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤝 Хотите стать нашим клиентом")
        ],
        [
            KeyboardButton(text="☕️ Хотите записаться на встречу")
        ],
        [
            KeyboardButton(text="🍻 Обсудим за пивом")
        ],
        [
            KeyboardButton(text="🎓 Нужна консультация")
        ]
    ],
    resize_keyboard=True
)
