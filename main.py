"""
This is an echo and id bot.
It echoes any incoming text messages and user id.
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message


API_TOKEN = '5744148618:AAHJx5JqdqSUtEBXfa2oH2XSx3pcUx9eJvo'


# Configure logging 
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    
    """
    This handler will be called when user sends `/start` command
    """

    await message.reply('Hi! This is a test bot on aiogram by @kvmvkxnt.')


@dp.message_handler()
async def echo(message: Message):

    # old style:
    # await bot.send_message(message.from_user.id, message.text)

    msg = f"{message.from_user.id}: {message.text}"

    await message.answer(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
