import asyncio
from datetime import datetime

from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

bot = Bot(token="")
dp = Dispatcher()



@dp.message(CommandStart())
async def on_start(message: Message):
    await message.answer(f"Hello {message.from_user.username}")


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "Commands:\n"
        "start - start the bot\n"
        "help - help\n"
        "time - current time\n"
    )

@dp.message(F.text == "Hi")
async def on_hi(message: Message):
    await message.reply(f"Hello {message.from_user.username}, how are you?")

@dp.message(Command('time'))
async def time(message: Message):
    now = datetime.now().strftime("%H:%M")
    await message.answer(f"Now is the time: {now}")



@dp.message()
async def on_message(message: Message):
    await message.answer(
        message.text.upper(),
    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())