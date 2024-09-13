from aiogram import types


kb = [
    [types.KeyboardButton(text="exit")],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

#TODO Доделать клавиатуру