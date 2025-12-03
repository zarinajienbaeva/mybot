from aiogram import Bot, Dispatcher , F
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.filters import Command
from config import token
import asyncio

my_bot = Bot(token=str(token))
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(f"Welcome, {message.from_user.full_name} ")

@dp.message(Command("info", prefix="!/"))
async def handle_info(message: types.Message):
    await message.answer(text="This is a test bot for learning aiogram ")



@dp.message(F.photo)
async def handle_photo(message: types.Message):
    await message.copy_to(chat_id=message.chat.id)



async def main():
    print("I am starting ...")
    await dp.start_polling(my_bot)



if __name__ == "__main__":
    asyncio.run(main())