from aiogram import types
from loader import dp

# sdfg sdfs dfgs dfg
@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(message.text)
