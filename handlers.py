from aiogram import F, Router, types
from aiogram.types import Message,InputFile 
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import logging

import keyboard as kb

# Настройка логирования
logging.basicConfig(level=logging.INFO)

router = Router()

class Register(StatesGroup):
     name = State()
     username = State()
     type_art = State()
     background_art = State()
     term_of_work = State()
     additional_factors_art = State()
     your_comments = State()  

@router.message(Command('start'))
async def cmd_start(message: Message):
         await message.answer("Привет! Рада тебя видеть! 😊 Я занимаюсь созданием уникальных артов и скетчей. Если у тебя есть идея, могу помочь её реализовать. О чем ты думаешь?", reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
        await message.answer('Ты нажал на кнопку помощи.')

@router.message(Command('contact'))
async def cmd_help(message: Message):
        await message.answer('Создатель бота 💻- @Billy_WL , художник 🖌️- @Enotkruty')

@router.message(F.text == 'Как можно заказать арт?')
async def order_art(message: Message):
        await message.answer('Заказать очень просто! Через команду /register')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('1. Введи свое имя.')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.username)
    await message.answer('2. Введи свой юзернейм, чтобы автор скинул вам работу, когда она будет готова.')

@router.message(Register.username)
async def register_username(message: Message, state: FSMContext):
   await state.update_data(username=message.text)
   await state.set_state(Register.type_art)
   await message.answer('3. Полноценная работа/Скетч(набросок)?')

@router.message(Register.type_art)
async def register_type_art(message: Message, state: FSMContext):
   await state.update_data(type_art=message.text)
   await state.set_state(Register.background_art)
   await message.answer('4. Фон:\n 1. с простой заливкой\n 2. без сильной проработанности/рендеринга\n 3. коллаж')

@router.message(Register.background_art)
async def register_background_art(message: Message, state: FSMContext):
   await state.update_data(background_art=message.text)
   await state.set_state(Register.term_of_work)
   await message.answer('5. Срок: (+30% за срочность; дедлайн: от 2 недель до месяца)')

@router.message(Register.term_of_work)
async def register_term_of_work(message: Message, state: FSMContext):
   await state.update_data(term_of_work=message.text)
   await state.set_state(Register.additional_factors_art)
   await message.answer('6. Дополнительные факторы:\n 1. второй персонаж\n 2. излишняя детализация\n 3. сложный ракурс')

@router.message(Register.additional_factors_art)
async def register_additional_factors_art(message: Message, state: FSMContext):
   await state.update_data(additional_factors_art=message.text)
   await state.set_state(Register.your_comments)
   await message.answer('7. Свои комментарии.')

@router.message(Register.your_comments)
async def register_your_comments(message: Message, state: FSMContext):
   await state.update_data(your_comments=message.text)

   data = await state.get_data()
   await message.answer(f'📌\nИмя: {data["name"]}\nЮзернейм: {data["username"]}\nТип: {data["type_art"]}\nФон: {data["background_art"]}\nCрок: {data["term_of_work"]}\nДополнительные факторы: {data["additional_factors_art"]}\nСвои комментарии: {data["your_comments"]}')
   await state.clear()


@router.message(F.text == 'Оплата')
async def payment(message: Message):
        await message.answer('Оплата происходит исключительно в рублях и в Сбербанк.')

@router.message(F.text == 'Цена')
async def price(message: Message):
        await message.answer(
            'Ознакомься с расценками:\n'
            '\t1. Скетч-арт с плоским покрасом: хед - 150₽, по пояс - 300₽, полнорост - 500₽;\n'
            '\t2. Полноценный арт: хед - 300₽, по пояс - 600₽, полнорост - 1000₽;\n' 
            '\t2.1. Полноценный арт с фоном(с учетом рендеринга под него): хед - 450₽, по пояс - 700₽, полнорост - 1500₽;\n'
            '\t3. Фон: 1. с простой заливкой - без оплаты 2. без сильной проработанности/рендеринга + 100-250₽ к <<полноценный арт>> 3.коллаж + 70₽ к <<полноценный арт>> ;\n'
            '\t4. Дополнительные факторы: 1. излишняя детализированность + к оплате 2. сложный ракурс + к оплате 3. + персонаж 100% оплаты ;\n'
        )

@router.message(F.text == 'Примеры работ')
async def example_arts(message: Message):
    await message.answer('Конечно! У меня есть портфолио с последними проектами. Если тебе нужно что-то конкретное, дай знать — я помогу найти примеры, которые могут тебя вдохновить. Tgc: https://t.me/Zuzucut')

@router.message(F.text == 'Срок')
async def term_of_work (message: Message):
        await message.answer('Обычно это занимает от 2 недель до месяца, в зависимости от сложности. После того как обсудим детали, я смогу сказать более точно. А у тебя есть конкретные сроки на примете?')

@router.message(F.text == 'Отзывы от клиентов')
async def customer_reviews(message: Message):
        await message.answer('Да, конечно! Я собираю отзывы от клиентов, и они есть на сайте. Если интересно, можешь почитать, что люди говорят о моей работе. Если у тебя есть еще вопросы, всегда рада помочь!')