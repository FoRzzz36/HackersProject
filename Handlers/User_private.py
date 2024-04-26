from aiogram import types, Router, F, Bot
from aiogram.filters import CommandStart, or_f

from kb.inline import get_agree_button, get_choice_mod, get_back_button, get_cities_menu_keyboard, \
    get_type_menu_keyboard, get_placesmenu_by_parms, get_info_about_place
from settings import Places

UserPrivate = Router()

IsAgree = False
PlacePar=[None,None]
photo_to_del=None

@UserPrivate.message(F.photo)
async def get_photo(msg: types.Message):
    await msg.answer(f'ID фото: {msg.photo[-1].file_id}')
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
    await callback.message.answer('Добро пожаловать в Калининградскую область👋', reply_markup=get_choice_mod())
    await callback.message.delete()

@UserPrivate.callback_query(F.data == "card_work")
async def cardwork_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Карта гостя Калининградской области – программа лояльности, '
                                  'благодаря которой туристы получают приятные бонусы и скидки на лучшие '
                                  'туристические предложения региона!\nКарта действует в заведениях-участниках '
                                  'программы, скидкой можно воспользоваться однократно', reply_markup=get_back_button(1))

@UserPrivate.callback_query(or_f(F.data == "back_1", F.data == "back_2"))
async def back12_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Добро пожаловать в Калининградскую область👋', reply_markup=get_choice_mod())

@UserPrivate.callback_query(F.data == "start_work")
async def startwork_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберете город в котором хотите отдохнуть:', reply_markup=get_cities_menu_keyboard())

#@UserPrivate.callback_query(F.data == "klgd" or F.data == "zel" or F.data == "sve" or F.data == 'yant' or F.data == "pol" or F.data == "cher")
@UserPrivate.callback_query(or_f(F.data == "klgd", F.data == "zel", F.data == "sve", F.data == 'yant',
                                 F.data == "pol", F.data == "cher", F.data == "all_cyt"))
async def citiesmenu_handle(callback: types.CallbackQuery):
    await callback.answer()
    PlacePar[0]=callback.data
    await callback.message.edit_text('Выберете как вы хотите отдохнуть:', reply_markup=get_type_menu_keyboard())

@UserPrivate.callback_query(or_f(F.data == "kult", F.data ==  "ent", F.data ==  "food", F.data ==  'liv', F.data ==  "driv",
                            F.data == "SPA", F.data == "suv", F.data == "tur", F.data == "all_typ"))
async def typemenu_handle(callback: types.CallbackQuery):
    await callback.answer()
    PlacePar[1]=callback.data
    await callback.message.edit_text('Выберете интересюющие место:', reply_markup=get_placesmenu_by_parms(PlacePar))

@UserPrivate.callback_query(F.data == "back_3")
async def back3_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберете город в котором хотите отдохнуть:',
                                     reply_markup=get_cities_menu_keyboard())
@UserPrivate.callback_query(F.data == "back_4")
async def back4_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберете как вы хотите отдохнуть:', reply_markup=get_type_menu_keyboard())

@UserPrivate.callback_query(or_f(F.data == '0', F.data == '1', F.data== '2', F.data == '3', F.data== '4', F.data == '5', F.data== '6', F.data == '7', F.data== '8', F.data == '9', F.data== '10', F.data == '11', F.data== '12'))
async def place_info_handle(callback: types.CallbackQuery, bot : Bot):
    await callback.answer()
    place_now=Places[int(callback.data)]
    await callback.message.edit_text(f"CКИДКА {place_now[4]}%!!\n{place_now[0]} - это {place_now[2]}.\nНаходится по адрессу: {place_now[1]}.\n"
                                     f"Подробнее про это вы можете узнать на нашем сайте: {place_now[3]}\nХотите оставить отзыв об этом месте?", reply_markup=get_info_about_place(place_now))

@UserPrivate.callback_query(F.data == "back_5")
async def back5_handle(callback: types.CallbackQuery, bot : Bot):
    await callback.answer()
    await callback.message.edit_text('Выберете интересюющие место:', reply_markup=get_placesmenu_by_parms(PlacePar))
    await bot.delete_message(callback.message.chat.id, callback.message.message_id+1)