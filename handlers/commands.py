from aiogram.types import Message
from config import dp
from keyboards import main_kb

@dp.message_handler(commands="start",state="*")
async def started(message:Message):
    await message.answer(f"Assalom aleykum {message.chat.full_name}\nBu tarjimon bot\nKerakli tugmani bosing",reply_markup=main_kb)

@dp.message_handler(commands="help")
async def helped(message:Message):
    await message.answer("Botdan foydalanish uchun ...")
    