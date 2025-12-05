from aiogram import F, Router, types
from config import my_id  

router = Router()

@router.message(F.from_user.id == my_id)
async def handle_my_messages(message: types.Message):
    
    text = message.text.strip()

    words = text.split()
    if len(words) == 1:
        await message.answer(f"So'z uzunligi: {len(text)} ta belgi")
    else:
        await message.answer(f"Siz yuborgan matn: {text}")
