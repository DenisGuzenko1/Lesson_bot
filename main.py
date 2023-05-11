from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from keyboard import start,inline_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import config  # импортируем файл config
import logging  # модуль для вывода инфы


storage = MemoryStorage()
bot = Bot(token=config.bot_key, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.basicConfig(
    # указываем название с логами
    filename='log.txt',
    # указываем уровень логирования
    level=logging.INFO,
    # указываем формат сохранения логов
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s'))

@dp.message_handler(Command('start'), state=None)  # задаем название команды старт
async def welcome(message):
    joined_file = open('user.txt', 'r')
    joined_users = set()
    for line in joined_file:
        joined_users.add(line.strip())
    if not str(message.chat.id) in joined_users:
        joined_file = open('user.txt', 'a')
        joined_file.write(str(message.chat.id) + '\n')
        joined_users.add(message.chat.id)
    await bot.send_message(message.chat.id, f'ПРИВЕТ, *{message.from_user.first_name},* БОТ РАБОТАЕТ',
                           reply_markup=start, parse_mode='Markdown')
    # после проверки и записи выводим сообщения с именем пользователя и выводим кнопки
@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == 'Информация':
        await bot.send_message(message.chat.id, text = 'Информация\nБот создан специально для обучения', \
                               parse_mode='Markdown')

@dp.message_handler(commands=['links'])
async def url_command(message):
    await message.answer(text='Ссылочки', reply_markup=inline_kb)


if __name__ == '__main__':
    print('Бот запущен')
    executor.start_polling(dispatcher=dp, skip_updates=True)