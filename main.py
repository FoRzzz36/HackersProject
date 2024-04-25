from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '7063519009:AAHNi0LH9GRgoLP50izsNPFHEWAQYAD'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем. 
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Эхо-бот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.") #Так как код работает асинхронно, то обязательно пишем await.