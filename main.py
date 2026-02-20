import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from app.handlers import router 

# Конфигурация
API_TOKEN = ''  
NUM_USERS = 100  

# Инициализация бота и диспетчера с хранилищем состояний (FSM)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=storage)

async def main():
    # Подключаем роутер с обработчиками
    dp.include_router(router)
    # Запускаем поллинг
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')
