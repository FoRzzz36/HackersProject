import sqlite3
from aiogram import types, Router, F, Bot
from aiogram.filters import or_f, StateFilter
from aiogram.fsm.context import FSMContext
from kb.inline import get_choice_mod, get_back_button, get_cities_menu_keyboard, \
    get_type_menu_keyboard, get_placesmenu_by_parms, get_info_about_place, get_choice_rate
from settings import Places, blank_photo
from Forms import FormRate_bot


#**********************************************************************ДБ**************************************************************
connection = sqlite3.connect("TouristBotStatistics.db")
connection.execute("PRAGMA Journal_mode=WAL")
cursor = connection.cursor()
def CityCode(s):
    if s == 'klgd':
        return('Калининград ')
    if s == 'zel':
        return('Зеленоградск')
    if s == 'sve':
        return('Светлогорск ')
    if s == 'yant':
        return('Янтарный    ')
    if s == 'pol':
        return('Полесск     ')
    if s == 'cher':
        return('Черняховск  ')
#таблица visit
def add_visitor(s): #добавть посетителя
    cursor.execute('SELECT count FROM visit WHERE location = ?', (s, ))
    users = cursor.fetchone()
    cursor.execute('UPDATE visit SET count = ? WHERE location = ?', (int(users[0]) + 1, s))
    connection.commit()
def print_visit(): #вывести всё из visit
    cursor.execute('SELECT * FROM visit')
    users = cursor.fetchall()
    for user in users:
        print(user)
#таблица places
def change_sale(id, s):
    try:
        cursor.execute('UPDATE places SET sale = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_name(id, s):
    try:
        cursor.execute('SELECT * FROM visit')
        res = cursor.fetchall()
        cursor.execute('SELECT Name FROM places WHERE id = ?', (id, ))
        a = cursor.fetchone()
        k = a[0] #имя с данным id
        cursor.execute('SELECT City FROM places WHERE id = ?', (id, ))
        b = cursor.fetchone()
        m = b[0] #код города с данным id
        for r in res:
            t = r[0]
            if t[0: len(t) - 15] == k and t[len(t)-13:len(t)-1] == CityCode(m):
                d = t.replace(k, s)
                cursor.execute('UPDATE visit SET location = ? WHERE location = ?', (d, r[0]))
        cursor.execute('UPDATE places SET Name = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_address(id, s):
    try:
        cursor.execute('UPDATE places SET Address = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_desc(id, s):
    try:
        cursor.execute('UPDATE places SET desc = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_link(id, s):
    try:
        cursor.execute('UPDATE places SET link = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_city(id, s):
    try:
        cursor.execute('SELECT * FROM visit')
        res = cursor.fetchall()
        cursor.execute('SELECT Name FROM places WHERE id = ?', (id, ))
        a = cursor.fetchone()
        k = a[0] #имя с данным id
        cursor.execute('SELECT City FROM places WHERE id = ?', (id, ))
        b = cursor.fetchone()
        m = b[0] #код города с данным id
        for r in res:
            t = r[0]
            if t[0: len(t) - 15] == k and t[len(t)-13:len(t)-1] == CityCode(m):
                d = t.replace(CityCode(m), CityCode(s))
                cursor.execute('UPDATE visit SET location = ? WHERE location = ?', (d, r[0]))
        cursor.execute('UPDATE places SET City = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_type(id, s):
    try:
        cursor.execute('UPDATE places SET type = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def print_places():
    cursor.execute('SELECT * FROM places')
    users = cursor.fetchall()
    for user in users:
        print(user)
#таблица rating
def print_rating():
    cursor.execute('SELECT * FROM rating')
    users = cursor.fetchall()
    for user in users:
        print(user)
def Insert_rating(i):
    cursor.execute('SELECT number FROM rating WHERE rtng = ?', (i, ))
    res = cursor.fetchone()
    cursor.execute('UPDATE rating SET number = ? WHERE rtng = ?', (int(res[0]) + 1, i))
    connection.commit()
def output():
    connection.close()

#**************************************************************************************************************************************
UserPrivate = Router()

IsAgree = False
PlacePar=[None,None]
photo_to_del=None

city_code={'klgd':'Калининград', 'zel':'Зеленоградск', 'sve':'Светлогорск', 'yant':'Янтарный', 'pol':'Полесск', 'cher':'Черняховск'}

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
                                     f"Подробнее про это вы можете узнать на нашем сайте: {place_now[3]}\n"
                                                f"Хотите оставить отзыв об этом месте?", reply_markup=get_info_about_place(place_now))

@UserPrivate.callback_query(F.data == "back_5")
async def back5_handle(callback: types.CallbackQuery, bot : Bot):
    await callback.answer()
    await callback.message.edit_media(media=types.InputMediaPhoto(media=blank_photo))
    await callback.message.edit_caption(caption='Выберете интересюющие место:', reply_markup=get_placesmenu_by_parms(PlacePar))
    await bot.delete_message(callback.message.chat.id, callback.message.message_id+1)

@UserPrivate.callback_query(F.data == 'rate_work', StateFilter(None))
async def change_sale(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_caption(caption='Сколько звёзд вы нам поставите?', reply_markup=get_choice_rate())

@UserPrivate.callback_query(F.data.contains('rate_work_'), StateFilter(None))
async def change_sale(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_caption(caption='Пожалуйста, напишите чтобы вы хотели исправить/улучшить в нашем боте.\nНам важно ваше мнение!', reply_markup=get_back_button(6))
    await state.set_state(FormRate_bot.msg)
    await state.update_data(rate=int(callback.data[-1]))

@UserPrivate.callback_query(F.data == "back_6")
async def back6_handle(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_caption(caption='Сколько звёзд вы нам поставите?', reply_markup=get_choice_rate())
    await state.clear()

@UserPrivate.message(F.text, FormRate_bot.msg)
async def change_sale(message: types.Message, state: FSMContext):
    # try:
    data = await state.get_data()
    Insert_rating(data['rate'])
    await state.clear()
    await message.answer_photo(blank_photo, 'Данные успешно изменены!✅', reply_markup=get_back_button(2))
    # except:
    #     await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')