from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import logging
import asyncio
import wikipedia
from keyboards import buttons
from dotenv import load_dotenv
import os

dp = Dispatcher()

@dp.startup()
async def startup_answer(bot: Bot):
    await bot.send_message(5230484991, "Bot ishga tushdi")

@dp.message(CommandStart())
async def start(message: types.Message):
    global msg
    msg = await message.answer(f"Tilni tanlang | choose language | Выберите язык", reply_markup=buttons)

@dp.callback_query()
async def callback(call: types.CallbackQuery):
    if call.data == "uz":
        msg.delete()
        wikipedia.set_lang("uz")
        await call.message.answer(f"Salom {call.message.from_user.full_name}\nmen wikipedia bot\nmen maqola topishim uchun menga maqolaga oid bo'lgan mavzuni yuboring")
        await bot.set_my_commands([types.BotCommand("start", "Botni ishga tushurish")])
    elif call.data == "en":
        msg.delete()
        wikipedia.set_lang("en")
        await call.message.answer(f"Hello {call.message.from_user.full_name}\nI'm wikipedia bot\nI can search for wikipedia articles")
        await bot.set_my_commands([types.BotCommand("start", "start the bot")])
    elif call.data == "ru":
        msg.delete()
        wikipedia.set_lang("ru")
        await call.message.answer(f"Здравствуйте {call.message.from_user.full_name}\nя бот wikipedia\nя могу искать статьи в википедии")
        await bot.set_my_commands([types.BotCommand("start", "начать бота")])

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
    global bot

    load_dotenv()

    bot = Bot(os.getenv("BOT_TOKEN"))

    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())