from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_agree_button():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Прочитано✅", callback_data="agree")
    return keyboard_builder.as_markup()