from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import logging
import asyncio
import wikipedia
from keyboards import buttons

wikipedia.set_lang('uz')
bot = Bot("5904607271:AAH-edy50mxak7BhgfeCB-9oLnlrK5QMPiM")
dp = Dispatcher()

@dp.startup()
async def startup_answer(bot: Bot):
    await bot.send_message(5230484991, "Bot ishga tushdi")

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}\nmen wikipedia bot\nmen maqola topishim uchun menga maqolaga oid bo'lgan mavzuni yuboring")

@dp.message()
async def function(message: types.Message):
    try:
        await message.answer(wikipedia.summary(message.text))
    except Exception as e:
        await message.answer("Bu mavzuga oid maqola topilmadi")
TypeError
@dp.shutdown()
async def shut_down(bot: Bot):
    await bot.send_message(5230484991, "Bot to'xtadi")

async def main():
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())