from aiogram import Dispatcher

from tgbot.handlers.echo import register_echo_handlers


def register_all_handlers(dp: Dispatcher):
    register_echo_handlers(dp)