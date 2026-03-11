import asyncio

from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

bot = Bot(token="")
dp = Dispatcher()



@dp.message(CommandStart())
async def on_start(message: Message):
    await message.answer(f"Hello {message.from_user.username}")

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