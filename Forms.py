from aiogram.fsm.state import State, StatesGroup

class FormCName(StatesGroup):
    new_name = State()

class FormCSale(StatesGroup):
    new_sale = State()

class FormCAdress(StatesGroup):
    new_adress = State()

class FormCLink(StatesGroup):
    new_link = State()

class FormCCity(StatesGroup):
    new_city = State()

class FormCType(StatesGroup):
    new_type = State()

class FormCDesc(StatesGroup):
    new_desc = State()

class FormCImg(StatesGroup):
    new_img = State()

class FormRate_bot(StatesGroup):
    msg = State()