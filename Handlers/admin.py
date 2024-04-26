from aiogram import types, Router, F, Bot
from aiogram.filters import CommandStart, or_f

from kb.inline import get_agree_button, get_choice_mod, get_back_button, get_cities_menu_keyboard, \
    get_type_menu_keyboard, get_placesmenu_by_parms, get_info_about_place
from settings import Places

Admin = Router()

