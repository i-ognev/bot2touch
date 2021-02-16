from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer("Извините, но я Вас не понимаю. Возможно,"
                         " вы не выбрали нужный пункт или набрали несуществующую команду!")
