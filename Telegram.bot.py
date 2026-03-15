import asyncio
from datetime import datetime
import random
import telebot


from aiogram import F, Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command

bot = Bot(token="")
dp = Dispatcher()


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Profile")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def on_start(message: Message):
    await message.answer(f"Hello {message.from_user.username}")
    await message.answer("Main menu", reply_markup=menu)


@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "Commands:\n"
        "/start - start the bot\n"
        "/help - help\n"
        "/time - current time\n"
        "/game - start a game\n"
    )


@dp.message(Command('time'))
async def time(message: Message):
    now = datetime.now().strftime("%H:%M")
    await message.answer(f"Now is the time: {now}")

@dp.message(F.text == "Profile")
async def profile(message: Message):

    user_id = message.from_user.id
    user_name = message.from_user.username
    name = message.from_user.first_name

    text = f"""
    Yoy profile
    ID: {user_id}
    Name: {name}
    Username: {user_name}
    """

    await message.answer(text)

@dp.message(F.text == "Hi")
async def on_hi(message: Message):
    await message.reply(f"Hello {message.from_user.username}, how are you?")


@dp.message()
async def on_message(message: Message):
    await message.answer(
        message.text.upper(),
    )












async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
