from aiogram import types, Router, F, Bot
from aiogram.filters import CommandStart, or_f

from kb.inline import get_agree_button, get_choice_mod, get_back_button, get_cities_menu_keyboard, \
    get_type_menu_keyboard, get_placesmenu_by_parms, get_info_about_place
from settings import Places, blank_photo

UserPrivate = Router()

IsAgree = False
PlacePar=[None,None]
photo_to_del=None


# @UserPrivate.message(CommandStart())
# async def start_cmd(message: types.Message):
#     await message.answer('Рады приветствовать вас в нашей области!👋 Этот бот поможет вам узнать сумму скидки на любой вид '
#                          'услуг в нашей области!Представителями которых являются наши партнёры)')
#     await message.answer('Помните:\n  *Срок действия карты не ограничен, а скидки и предложения по карте гостя '
#                          'обновляются ежегодно.\n  *Пользоваться картой могут только гости города. '
#                          'Карту гостя необходимо предоставлять заранее до оплаты услуг и заключения договоров.\n'
#                          '(нажмите "почитано", чтобы продолжить работу с ботом)', reply_markup=get_agree_button())

@UserPrivate.callback_query(F.data == "agree")
async def agree_handle(callback: types.CallbackQuery):
    await callback.answer()
    IsAgree = True
    await callback.message.answer_photo(blank_photo, 'Добро пожаловать в Калининградскую область👋', reply_markup=get_choice_mod())
    await callback.message.delete()

@UserPrivate.callback_query(F.data == "card_work")
async def cardwork_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption='Карта гостя Калининградской области – программа лояльности, '
                                  'благодаря которой туристы получают приятные бонусы и скидки на лучшие '
                                  'туристические предложения региона!\nКарта действует в заведениях-участниках '
                                  'программы, скидкой можно воспользоваться однократно', reply_markup=get_back_button(1))

@UserPrivate.callback_query(or_f(F.data == "back_1", F.data == "back_2"))
async def back12_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption='Добро пожаловать в Калининградскую область👋', reply_markup=get_choice_mod())

@UserPrivate.callback_query(F.data == "start_work")
async def startwork_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption='Выберете город в котором хотите отдохнуть📂:', reply_markup=get_cities_menu_keyboard())


@UserPrivate.callback_query(or_f(F.data == "klgd", F.data == "zel", F.data == "sve", F.data == 'yant',
                                 F.data == "pol", F.data == "cher", F.data == "all_cyt"))
async def citiesmenu_handle(callback: types.CallbackQuery):
    await callback.answer()
    PlacePar[0]=callback.data
    await callback.message.edit_caption(caption='Выберете как вы хотите отдохнуть📂:', reply_markup=get_type_menu_keyboard())

@UserPrivate.callback_query(or_f(F.data == "kult", F.data ==  "ent", F.data ==  "food", F.data ==  'liv', F.data ==  "driv",
                            F.data == "SPA", F.data == "suv", F.data == "tur", F.data == "all_typ"))
async def typemenu_handle(callback: types.CallbackQuery):
    await callback.answer()
    PlacePar[1]=callback.data
    await callback.message.edit_caption(caption='Выберете интересюющие место📂:', reply_markup=get_placesmenu_by_parms(PlacePar))

@UserPrivate.callback_query(F.data == "back_3")
async def back3_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption='Выберете город в котором хотите отдохнуть📂:',
                                     reply_markup=get_cities_menu_keyboard())
@UserPrivate.callback_query(F.data == "back_4")
async def back4_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption='Выберете как вы хотите отдохнуть📂:', reply_markup=get_type_menu_keyboard())

@UserPrivate.callback_query(or_f(F.data == '0', F.data == '1', F.data== '2', F.data == '3', F.data== '4', F.data == '5',
                                 F.data== '6', F.data == '7', F.data== '8', F.data == '9', F.data== '10', F.data == '11',
                                 F.data== '12', F.data == '13', F.data == '14', F.data== '15', F.data == '16', F.data== '17',
                                 F.data == '18', F.data== '19', F.data == '20', F.data== '21', F.data == '22', F.data== '23',
                                 F.data == '24', F.data== '25', F.data== '26', F.data == '27', F.data== '28', F.data == '29',
                                 F.data== '30', F.data == '31', F.data== '32', F.data == '33', F.data == '34', F.data== '35',
                                 F.data == '36', F.data== '37', F.data == '38', F.data== '39', F.data == '40', F.data== '41',
                                 F.data == '42'))
async def place_info_handle(callback: types.CallbackQuery, bot : Bot):
    await callback.answer()
    place_now=Places[int(callback.data)]
    await callback.message.edit_media(media=types.InputMediaPhoto(media=Places[int(callback.data)][7]))
    await callback.message.edit_caption(caption=f"CКИДКА {place_now[4]}%!!\n{place_now[0]} - это {place_now[2]}.\n"
                                     f"Находится по адрессу: {place_now[1]}.\n"
                                     f"Подробнее про это вы можете узнать на нашем сайте: {place_now[3]}\
                                     nХотите оставить отзыв об этом месте?", reply_markup=get_info_about_place(place_now))

@UserPrivate.callback_query(F.data == "back_5")
async def back5_handle(callback: types.CallbackQuery, bot : Bot):
    await callback.answer()
    await callback.message.edit_media(media=types.InputMediaPhoto(media=blank_photo))
    await callback.message.edit_caption(caption='Выберете интересюющие место:', reply_markup=get_placesmenu_by_parms(PlacePar))
    await bot.delete_message(callback.message.chat.id, callback.message.message_id+1)