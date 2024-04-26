import asyncio
from aiogram import Bot, Dispatcher, types
import random
from settings import TOKEN, Places
from Handlers.User_private import UserPrivate
from aiogram.filters import CommandStart

from kb.inline import get_admin_choice_mod, get_agree_button
from Handlers.admin import Admin
from settings import ADMIN_LIST, Sticker_list

bot=Bot(token=TOKEN)


ALLOWED_UPDATES = ['message, edited_message']
dp=Dispatcher()

dp.message()
#dp.include_router(UserPrivate)
#dp.include_router(Admin)

@dp.message(CommandStart())
async def show_id(msg: types.Message):
    await msg.answer_sticker(random.choice(Sticker_list))
    if msg.from_user.id in ADMIN_LIST:
        await msg.answer('Доброго времени суток! Какие изменения мы хотим внести на этот раз?🤔',
                             reply_markup=get_admin_choice_mod())
        dp.include_router(Admin)
    else:
        await msg.answer(
            'Рады приветствовать вас в нашей области!👋 Этот бот поможет вам узнать сумму скидки на любой вид '
            'услуг в нашей области!Представителями которых являются наши партнёры)')
        await msg.answer('Помните:\n  *Срок действия карты не ограничен, а скидки и предложения по карте гостя '
                             'обновляются ежегодно.\n  *Пользоваться картой могут только гости города. '
                             'Карту гостя необходимо предоставлять заранее до оплаты услуг и заключения договоров.\n'
                             '(нажмите "почитано", чтобы продолжить работу с ботом)', reply_markup=get_agree_button())
        dp.include_router(UserPrivate)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())