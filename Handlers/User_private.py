from aiogram import types, Router, F
from aiogram.filters import CommandStart

from kb.inline import get_agree_button
UserPrivate = Router()

IsAgree = False
@UserPrivate.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Приветствие')
    await message.answer('Помните:\n  *Срок действия карты не ограничен, а скидки и предложения по карте гостя '
                         'обновляются ежегодно.\n  *Пользоваться картой могут только гости города. '
                         'Карту гостя необходимо предоставлять заранее до оплаты услуг и заключения договоров.\n'
                         '(нажмите "почитано", чтобы продолжить работу с ботом)', reply_markup=get_agree_button())

@UserPrivate.callback_query(F.data == "agree")
async def agree_handle(callback: types.CallbackQuery):
    await callback.answer()
    IsAgree = True
    await callback.message.delete()

