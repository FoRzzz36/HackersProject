import asyncio
from aiogram import Bot, Dispatcher

from settings import TOKEN
from Handlers.User_private import UserPrivate

bot=Bot(token=TOKEN)
ALLOWED_UPDATES = ['message, edited_message']
dp=Dispatcher()

dp.include_router(UserPrivate)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())