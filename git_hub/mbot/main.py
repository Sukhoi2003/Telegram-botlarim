from aiogram import Bot, Dispatcher, executor, types
import pyqrcode

bot = Bot(token="6214945945:AAG2KaMqDZwxurWxmtvceJj4hARwDs6bo-A")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    await message.reply("Salom! Botimizga xush kelibsiz!\nSizga qanday yordambera olamiz")

@dp.message_handler(commands=["logo"])
async def logo(message: types.Message):
    await message.answer_photo("https://avatars.githubusercontent.com/u/126697665?s=400&u=5affbfd2640ff144a9fc7826cff6980032a20082&v=4")


@dp.message_handler()
async def qr(message: types.Message):
    text = pyqrcode.create(message.text)
    text.png("code.png", scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open("code.png", "rb"))


executor.start_polling(dp)