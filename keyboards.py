from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="O'zbekcha 🇺🇿", callback_data="uz")],
    [InlineKeyboardButton(text="English 🇬🇧", callback_data="en")],
    [InlineKeyboardButton(text="Русский 🇷🇺", callback_data="ru")]
])