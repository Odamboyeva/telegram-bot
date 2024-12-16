import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from button import * 
from config import BOT_TOKEN

bot = Bot(token= BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 
dp = Dispatcher()

@dp.message(Command("start"))
async def CommandStart(message: Message):
    await message.answer(f"Qanday maoshni hisoblaymiz?",reply_markup=menu)

#soatiga hisoblash
@dp.message(F.text == "Soatbay|Hisoblash⏳")
async def StartCommand(message: Message):
    await message.answer(caption = "Toifangizni tanlang|✍🏻:", reply_markup=soathisoblaw)


@dp.message(F.text == "Oliy|Toifa 👩🏻‍🎓🧑🏻‍🎓")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=soathisoblaw)


@dp.message(F.text == "1|Toifa1️⃣")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=soathisoblaw)


@dp.message(F.text == "2|Toifa2️⃣")
async def StartCommand(message: Message):
    await message.answer(caption = "2|Toifa2️⃣", reply_markup=soathisoblaw)


@dp.message(F.text == "Mutaxasis|🤓")
async def StartCommand(message: Message):
    await message.answer (caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=soathisoblaw)


@dp.message(F.text == "O'rta|Maxsus🤓")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=soathisoblaw)


@dp.message(F.text == "Bosh|Sahifa 🔙")
async def StartCommand(message: Message):
    await message.answer(reply_markup=menu)


#Bowlangich sinf
@dp.message(F.text == "Boshlang'ich|Sinf👧🏼👶🏼")
async def StartCommand(message: Message):
    await message.answer(caption = "Toifangizni tanlang:",reply_markup=bowlangich)


@dp.message(F.text == "Oliy|Toifa 👩🏻‍🎓🧑🏻‍🎓")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=bowlangich)


@dp.message(F.text == "1|Toifa1️⃣")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=bowlangich)


@dp.message(F.text == "2|Toifa2️⃣")
async def StartCommand(message: Message):
    await message.answer(caption = "2|Toifa2️⃣", reply_markup=bowlangich)


@dp.message(F.text == "Mutaxasis|🤓")
async def StartCommand(message: Message):
    await message.answer (caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=bowlangich)


@dp.message(F.text == "O'rta|Maxsus🤓")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=bowlangich)


@dp.message(F.text == "Bosh|Sahifa 🔙")
async def StartCommand(message: Message):
    await message.answer(reply_markup=menu)


#yuqori sinf uchun
@dp.message(F.text == "Yuqori|Sinf|Uchun 👱🏻‍♀️👱🏻")
async def StartCommand(message: Message):
    await message.answer(caption = "Toifangizni tanlang:",reply_markup=yuqorisinf)



@dp.message(F.text == "Oliy|Toifa 👩🏻‍🎓🧑🏻‍🎓")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=yuqorisinf)


@dp.message(F.text == "1|Toifa1️⃣")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=yuqorisinf)


@dp.message(F.text == "2|Toifa2️⃣")
async def StartCommand(message: Message):
    await message.answer(caption = "2|Toifa2️⃣", reply_markup=yuqorisinf)


@dp.message(F.text == "Mutaxasis|🤓")
async def StartCommand(message: Message):
    await message.answer (caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=yuqorisinf)


@dp.message(F.text == "O'rta|Maxsus🤓")
async def StartCommand(message: Message):
    await message.answer(caption = "1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=yuqorisinf)


@dp.message(F.text == "Bosh|Sahifa 🔙")
async def StartCommand(message: Message):
    await message.answer(reply_markup=yuqorisinf)


@dp.message(F.text == "Dekrat|Puli🤱🏼")
async def StartCommand(message: Message):
    await message.answer(caption = "Umumiy o'rtacha oyligingizni jo'nating (Начисления):", reply_markup=dekrat)


@dp.message(F.text == "Bosh|Sahifa 🔙")
async def StartCommand(message: Message):
    await message.answer(reply_markup=dekrat)





async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())