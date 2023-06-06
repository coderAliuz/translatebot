from aiogram.types import Message
from config import dp
from keyboards import lang_kb,back_kb,main_kb
from aiogram.dispatcher import FSMContext
from googletrans import Translator

@dp.message_handler(text="Tarjimon")
async def tarjimon_hand(message:Message,state:FSMContext):
    await message.answer("Tarjima qilmoqchi bo'lgan bo'limni tanla",reply_markup=lang_kb)
    await state.set_state("tarjimon")

@dp.message_handler(text="Ortga",state="tarjimon")
async def ortga(message:Message,state:FSMContext):
    await message.answer("Kerakli tugmani bosing",reply_markup=main_kb)
    await state.finish()

@dp.message_handler(text="uz->ru",state="tarjimon")
async def uz_ru(message:Message,state:FSMContext):
    await message.reply("O'zbekcha so'z kirit",reply_markup=back_kb)
    await state.set_state("uz-ru")

@dp.message_handler(state="uz-ru")
async def uz_ru_tarjimon(message:Message,state:FSMContext):
    text=message.text
    if text=="Ortga":
        await message.answer("Tarjima qilmoqchi bo'lgan bo'limni tanla",reply_markup=lang_kb)
        await state.set_state("tarjimon")
    else:
        t=Translator()
        tarjima=t.translate(text,src="uz",dest="ru").text
        await message.reply(tarjima)


@dp.message_handler(text="uz->en",state="tarjimon")
async def uz_en(message:Message,state:FSMContext):
    await message.reply("O'zbekcha so'z kirit",reply_markup=back_kb)
    await state.set_state("uz-en")

@dp.message_handler(state="uz-en")
async def uz_en_tarjimon(message:Message,state:FSMContext):
    text=message.text
    if text=="Ortga":
        await message.answer("Tarjima qilmoqchi bo'lgan bo'limni tanla",reply_markup=lang_kb)
        await state.set_state("tarjimon")
    else:
        t=Translator()
        tarjima=t.translate(text,src="uz",dest="en").text
        await message.reply(tarjima)
