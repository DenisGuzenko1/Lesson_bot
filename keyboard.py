from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основа для кнопок

info = types.KeyboardButton('Информация')  # кнопка информации
stats = types.KeyboardButton('Статистика')  # кнопка статистики
start.add(stats, info)  # добавляем кнопку в основу бота

inline_kb = InlineKeyboardMarkup(row_width=2)
new_info = InlineKeyboardButton(text='Ещё информация', url='https://itproger.com/news/10-interesnih-faktov-pro-python')
list_lit = InlineKeyboardButton(text='Интересная литература', url='https://itproger.com/news/10-interesnih-faktov-pro-python')
inline_kb.add(new_info).add(list_lit)




