#По видео
'''
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token='')
dp = Dispatcher()

@dp.message
async def cmd_start(message: Message):
    await message.answer('Привет! Рада тебя видеть! Я занимаюсь созданием уникальных артов и скетчей. Если у тебя есть идея, могу помочь её реализовать. О чем ты думаешь?')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
'''
'''
#немного измененно
import asyncio
from aiogram import Bot,Dispatcher  
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types
from app.handlers import router


# Создание маршрутизатора
router = Dispatcher()
# Конфигурация
NUM_USERS = 100  # Укажите количество пользователей, с которыми бот должен работать одновременно



async def start_bot():
    API_TOKEN = '7694495732:AAHXqiTD7UlKdhQcFOMD0-jTpxG7stZKoms'  # remember to replace with your actual token
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Регистрация маршрутов
    dp.include_router(router)    
    await dp.start_polling(bot)

# Запуск сервера
if __name__ == '__main__':
    # Запуск бота
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Бот выключен')
'''
'''
import asyncio
from aiogram import Bot, Dispatcher
from aiohttp import web
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types
from app.handlers import router

# Создание маршрутизатора
storage = MemoryStorage()
bot = Bot(token='7694495732:AAHXqiTD7UlKdhQcFOMD0-jTpxG7stZKoms')  # Please replace 'YOUR_BOT_TOKEN' with your actual bot token
dp = Dispatcher(storage=storage)

# Конфигурация
NUM_USERS = 100  # Укажите количество пользователей, с которыми бот должен работать одновременно

# Обработчик запросов
async def handler(request):
    user_id = request.match_info.get('user_id', "Anonymous")
    return web.Response(text=f"Hello, User {user_id}!")

async def start_bot():
    # Регистрация маршрутов
    # Here you should define your handlers/routes for the bot the right way depending on your application logic
    
    # Starting the bot polling
    await dp.start_polling(bot)

# Запуск сервера
if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Бот выключен')
'''
'''

#через DeepSeek
import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


async def start_bot():
    API_TOKEN = '7694495732:AAHXqiTD7UlKdhQcFOMD0-jTpxG7stZKoms'  # remember to replace with your actual token
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Бот выключен')'''

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types
from app.handlers import router  # Ensure this is your router containing handlers


# Конфигурация
NUM_USERS = 100  # Укажите количество пользователей, с которыми бот должен работать одновременно

# Создание экземпляра бота и диспетчера
API_TOKEN = '7694495732:AAHXqiTD7UlKdhQcFOMD0-jTpxG7stZKoms'  # remember to replace with your actual token
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def start_bot():
    # Регистрация маршрутов
    dp.include_router(router)    
    await dp.start_polling(bot)

# Запуск сервера
if __name__ == '__main__':
    # Запуск бота
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Бот выключен')

