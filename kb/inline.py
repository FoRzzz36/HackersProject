from aiogram.utils.keyboard import InlineKeyboardBuilder

from settings import Places
def get_agree_button():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Прочитано✅", callback_data="agree")
    return keyboard_builder.as_markup()

def get_back_button(s):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Назад↩", callback_data=f"back_{s}")
    return keyboard_builder.as_markup()

def get_choice_mod():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Напомнить как работает карта скидок", callback_data="card_work")
    keyboard_builder.button(text="Начать работу", callback_data="start_work")
    return keyboard_builder.adjust(1, 1).as_markup()

def get_cities_menu_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="🏛️🏟️ Калининград", callback_data="klgd")
    keyboard_builder.button(text="🐈🎄 Зеленогадск", callback_data="zel")
    keyboard_builder.button(text="🐌🌳 Светлогорск", callback_data="sve")
    keyboard_builder.button(text="🧉🏖️ Янтарный", callback_data='yant')
    keyboard_builder.button(text="🐟🏕️ Полесск", callback_data="pol")
    keyboard_builder.button(text="🚂🍺 Черняховск", callback_data="cher")
    keyboard_builder.button(text="✨ Все", callback_data="all_cyt")
    keyboard_builder.button(text="Назад↩", callback_data="back_2")
    return keyboard_builder.adjust(2, repeat=True).as_markup()

def get_type_menu_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="🏛️ Культурный досуг", callback_data="kult")
    keyboard_builder.button(text="🔥 Развлечения", callback_data="ent")
    keyboard_builder.button(text="🍽️ Питание", callback_data="food")
    keyboard_builder.button(text="🏠 Проживание", callback_data='liv')
    keyboard_builder.button(text="🚗 Порокат", callback_data="driv")
    keyboard_builder.button(text="💆 СПА", callback_data="SPA")
    keyboard_builder.button(text="🎁 Сувениы", callback_data="suv")
    keyboard_builder.button(text="🏕️ Турестические фирмы", callback_data="tur")
    keyboard_builder.button(text="✨ Все", callback_data="all_typ")
    keyboard_builder.button(text="Назад↩", callback_data="back_3")
    return keyboard_builder.adjust(2, repeat=True).as_markup()

def get_placesmenu_by_parms(rec):
    keyboard_builder = InlineKeyboardBuilder()
    flag=True
    for i in range(len(Places)):
        place_now=Places[i]
        if (place_now[5]==rec[0] or rec[0]=='all_cyt') and (place_now[6]==rec[1] or rec[1]=='all_typ'):
            flag=False
            keyboard_builder.button(text=place_now[0], callback_data=str(i))
    if flag:
        keyboard_builder.button(text="К сожалению, в этом городе нет подходящих мест под ваш запрос. Назад↩", callback_data=f"back_4")
    else:
        keyboard_builder.button(text="Назад↩", callback_data=f"back_4")
    return keyboard_builder.adjust(1, repeat=True).as_markup()

def get_info_about_place(place):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Оставить отзыв📊", callback_data="rate_place")
    keyboard_builder.button(text="Назад↩", callback_data="back_5")
    return keyboard_builder.adjust(1, 1).as_markup()
