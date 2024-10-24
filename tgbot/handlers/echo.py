from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.misc.states import Form


async def command_start_handler(message: Message, state: FSMContext):
    await message.answer(f"Привет! <b>Как тебя зовут</b>?", parse_mode="HTML")
    await state.set_state(Form.name)


async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Сколько тебе <b>лет</b>?", parse_mode="HTML")
    await state.set_state(Form.age)


async def get_age(message: Message, state: FSMContext):
    user_data = await state.get_data()
    name = user_data.get('name')
    await message.answer(f"Приятно познакомиться, <code>{name}</code>!\n"
                         f"Тебе <code>{message.text}</code> лет.\n\n\n"
                         "<i>Чтобы отправить эхо сообщение - введи</i><pre>/echo твое сообщение</pre>",
                         parse_mode="HTML")
    await state.clear()


async def echo_handler(message: Message) -> None:
    edited = message.text.replace('/echo', "")
    try:
        await message.answer(edited)
    except TypeError:
        await message.answer("Nice try!")


def register_echo_handlers(dp: Dispatcher):
    dp.message.register(command_start_handler, CommandStart())
    dp.message.register(get_name, Form.name)
    dp.message.register(get_age, Form.age)
    dp.message.register(echo_handler, Command(commands=['echo']))