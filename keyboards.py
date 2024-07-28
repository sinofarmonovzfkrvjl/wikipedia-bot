from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("O'zbekcha 🇺🇿", callback_data="uz")],
    [InlineKeyboardButton("English 🇬🇧", callback_data="en")],
    [InlineKeyboardButton("Русский 🇷🇺", callback_data="ru")]
])