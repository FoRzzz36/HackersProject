from aiogram import types, Router, F, Bot
from aiogram.filters import CommandStart, or_f, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from Forms import FormCType, FormCSale, FormCCity, FormCLink, FormCName, FormCAdress, FormCImg, FormCDesc
from kb.inline import get_admin_choice_mod, get_cities_menu_keyboard, \
    get_type_menu_keyboard, get_placesmenu_by_parms, get_info_about_place_to_change, get_back_button, get_admin_choice_stat_mod
from settings import Places

Admin = Router()

PlacePar=[None,None]
obj_now=[None]

@Admin.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Доброго времени суток! Какие изменения мы хотим внести на этот раз?🤔',
                         reply_markup=get_admin_choice_mod())

@Admin.callback_query(F.data == 'change_data')
async def change_data(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберете город объекта, в который хотите внести изменения📂:',
                                     reply_markup=get_cities_menu_keyboard())

@Admin.callback_query(F.data == "back_2")
async def back_2(callback = types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Доброго времени суток! Какие изменения мы хотим внести на этот раз?🤔',
                         reply_markup=get_admin_choice_mod())
@Admin.callback_query(or_f(F.data == "klgd", F.data == "zel", F.data == "sve", F.data == 'yant',
                                 F.data == "pol", F.data == "cher", F.data == "all_cyt"))
async def citiesmenu_handle(callback: types.CallbackQuery):
    await callback.answer()
    PlacePar[0]=callback.data
    await callback.message.edit_text('Выберете тип объекта, в который хотите внести изменения📂:',
                                     reply_markup=get_type_menu_keyboard())

@Admin.callback_query(F.data == "back_3")
async def back3_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберете город объекта, в который хотите внести изменения📂:',
                                     reply_markup=get_cities_menu_keyboard())

@Admin.callback_query(or_f(F.data == "kult", F.data ==  "ent", F.data ==  "food", F.data ==  'liv', F.data ==  "driv",
                            F.data == "SPA", F.data == "suv", F.data == "tur", F.data == "all_typ"))
async def typemenu_handle(callback: types.CallbackQuery):
    await callback.answer()
    PlacePar[1]=callback.data
    await callback.message.edit_text('Выберете интересюющий объект📂:',
                                     reply_markup=get_placesmenu_by_parms(PlacePar))

@Admin.callback_query(F.data == "back_4")
async def back4_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберете тип объекта, в который хотите внести изменения📂:',
                                     reply_markup=get_type_menu_keyboard())

@Admin.callback_query(or_f(F.data == '0', F.data == '1', F.data== '2', F.data == '3', F.data== '4', F.data == '5',
                                 F.data== '6', F.data == '7', F.data== '8', F.data == '9', F.data== '10', F.data == '11',
                                 F.data== '12', F.data == '13', F.data == '14', F.data== '15', F.data == '16', F.data== '17',
                                 F.data == '18', F.data== '19', F.data == '20', F.data== '21', F.data == '22', F.data== '23',
                                 F.data == '24', F.data== '25', F.data== '26', F.data == '27', F.data== '28', F.data == '29',
                                 F.data== '30', F.data == '31', F.data== '32', F.data == '33', F.data == '34', F.data== '35',
                                 F.data == '36', F.data== '37', F.data == '38', F.data== '39', F.data == '40', F.data== '41',
                                 F.data == '42'))
async def place_info_handle(callback: types.CallbackQuery, bot : Bot):
    await callback.answer()
    obj_now[0]=int(callback.data)
    place_now=Places[obj_now[0]]
    await callback.message.edit_text(f"CКИДКА {place_now[4]}%!!\n{place_now[0]} - это {place_now[2]}.\n"
                                     f"Находится по адрессу: {place_now[1]}.\n"
                                     f"Подробнее про это вы можете узнать на нашем сайте: {place_now[3]}\n"
                                     f"Хотите что-то изменить?📂",
                                     reply_markup=get_info_about_place_to_change(obj_now[0]))
@Admin.callback_query(F.data == "back_5")
async def back5_handle(callback: types.CallbackQuery, bot : Bot):
    await callback.answer()
    await callback.message.edit_text('Выберете интересюющие место:', reply_markup=get_placesmenu_by_parms(PlacePar))

@Admin.callback_query(F.data.contains('change_sale'), StateFilter(None))
async def change_sale(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Введите новую скидку:', reply_markup=get_back_button(6))
    await state.set_state(FormCSale.new_sale)

@Admin.callback_query(F.data == "back_6")
async def back6_handle(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    place_now = Places[obj_now[0]]
    await callback.message.edit_text(f"CКИДКА {place_now[4]}%!!\n{place_now[0]} - это {place_now[2]}.\n"
                                     f"Находится по адрессу: {place_now[1]}.\n"
                                     f"Подробнее про это вы можете узнать на нашем сайте: {place_now[3]}\n"
                                     f"Хотите что-то изменить?📂",
                                     reply_markup=get_info_about_place_to_change(obj_now[0]))
    await state.clear()

@Admin.message(F.text, FormCSale.new_sale)
async def change_sale(message: types.Message, state: FSMContext):
    try:
        Places[obj_now[0]][4] = int(message.text)
        await state.clear()
        await message.answer('Данные успешно изменены!✅', reply_markup=get_back_button(6))
    except:
        await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')

@Admin.callback_query(F.data.contains('change_adress'), StateFilter(None))
async def change_sale(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Введите новый адесс:', reply_markup=get_back_button(6))
    await state.set_state(FormCAdress.new_adress)

@Admin.message(F.text, FormCAdress.new_adress)
async def change_sale(message: types.Message, state: FSMContext):
    try:
        Places[obj_now[0]][1] = message.text
        await state.clear()
        await message.answer('Данные успешно изменены!✅', reply_markup=get_back_button(6))
    except:
        await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')

@Admin.callback_query(F.data.contains('change_link'), StateFilter(None))
async def change_sale(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Введите новую ссылку:', reply_markup=get_back_button(6))
    await state.set_state(FormCLink.new_link)

@Admin.message(F.text, FormCLink.new_link)
async def change_sale(message: types.Message, state: FSMContext):
    try:
        Places[obj_now[0]][3] = message.text
        await state.clear()
        await message.answer('Данные успешно изменены!✅', reply_markup=get_back_button(6))
    except:
        await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')

@Admin.callback_query(F.data.contains('change_name'), StateFilter(None))
async def change_sale(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Введите новое название:', reply_markup=get_back_button(6))
    await state.set_state(FormCName.new_name)

@Admin.message(F.text, FormCName.new_name)
async def change_sale(message: types.Message, state: FSMContext):
    try:
        Places[obj_now[0]][0] = message.text
        await state.clear()
        await message.answer('Данные успешно изменены!✅', reply_markup=get_back_button(6))
    except:
        await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')

@Admin.callback_query(F.data.contains('change_desc'), StateFilter(None))
async def change_sale(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Введите новое описание(оно должно начинаться со слова это):',
                                     reply_markup=get_back_button(6))
    await state.set_state(FormCDesc.new_desc)

@Admin.message(F.text, FormCDesc.new_desc)
async def change_sale(message: types.Message, state: FSMContext):
    try:
        Places[obj_now[0]][2] = message.text
        await state.clear()
        await message.answer('Данные успешно изменены!✅', reply_markup=get_back_button(6))
    except:
        await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')

@Admin.callback_query(F.data.contains('change_city'), StateFilter(None))
async def change_sale(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Введите код нового города:\n(Калининград-klgd; Зеленоградск-zel;\n'
                                     'Светлогорск-sve; Янтарный-yant;\nПолесск-pol; Черняховск-cher)', reply_markup=get_back_button(6))
    await state.set_state(FormCCity.new_city)

@Admin.message(F.text, FormCCity.new_city)
async def change_sale(message: types.Message, state: FSMContext):
    try:
        if message.text.lower() in {'klgd', 'zel', 'sve', 'yant', 'pol', 'cher'}:
            Places[obj_now[0]][5] = message.text
            await state.clear()
            await message.answer('Данные успешно изменены!✅', reply_markup=get_back_button(6))
        else:
            await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')
    except:
        await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')

@Admin.callback_query(F.data.contains('change_type'), StateFilter(None))
async def change_type(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Введите код нового типа:\n(Культурный досуг-kult; Развлечения-ent;\n'
                                     'Питание-food; Проживание-liv;\nПорокат-driv; СПА-SPA\n'
                                     'Сувениы-suv; Турестические фирмы-tur)', reply_markup=get_back_button(6))
    await state.set_state(FormCType.new_type)

@Admin.message(F.text, FormCType.new_type)
async def change_sale(message: types.Message, state: FSMContext):
    try:
        if message.text.lower() in {'kult', 'ent', 'food', 'liv', 'driv', 'spa', 'suv', 'tur'}:
            Places[obj_now[0]][6] = message.text
            await state.clear()
            await message.answer('Данные успешно изменены!✅', reply_markup=get_back_button(6))
        else:
            await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')
    except:
        await message.answer('Вы ввели неправильные данные❌\nПопробуйте еще раз:')

@Admin.callback_query(F.data == "show_stat")
async def back4_handle(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберете какую статистику вы хотите увидеть📊:',
                                     reply_markup=get_admin_choice_stat_mod())