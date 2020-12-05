from asyncio import sleep

import config, divination, emoji
from Module import Parser
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=config.token)
dp = Dispatcher(bot)
pars = Parser()
pars.ParseHoroscope(0)


@dp.message_handler(commands='start')  # start command with help
async def StartCommand(message: types.Message):
    await message.reply(
        "Привет, я Гороскоп Бот. В любой момент ты можешь получить от меня гороскоп на день. Для этого напиши 'гороскоп знак зодиака'")


@dp.message_handler(lambda message: message.text and 'бот' and '?' in message.text.lower())  # divination
async def BaseErrorHandler(message: types.Message):
    await message.reply(emoji.emojize("Хм... нужно подумать :thought_balloon:"))  # use smiles
    await sleep(1)
    await message.reply(divination.random_line())


@dp.message_handler(lambda message: message.text and 'гороскоп' == message.text.lower())  # help for horoscope
async def BaseErrorHandler(message: types.Message):
    await message.reply(
        'Для получения гороскопа введите ваш знак зодиака. Пример "Гороскоп овен". Гороскоп обновляеться каждый день')


@dp.message_handler(lambda message: message.text and 'гороскоп овен' in message.text.lower())
async def AriesHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(0))
    await bot.send_photo(message.chat.id, open("Data/aries.jpg", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп телец' in message.text.lower())
async def TaurusHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(1))
    await bot.send_photo(message.chat.id, open("Data/taurus.png", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп близнецы' in message.text.lower())
async def GeminiHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(2))
    await bot.send_photo(message.chat.id, open("Data/gemini.jpg", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп рак' in message.text.lower())
async def CancerHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(3))
    await bot.send_photo(message.chat.id, open("Data/cancer.jpg", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп лев' in message.text.lower())
async def LeoHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(4))
    await bot.send_photo(message.chat.id, open("Data/leo.jpg", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп дева' in message.text.lower())
async def VirgoHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(5))
    await bot.send_photo(message.chat.id, open("Data/virgo.png", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп весы' in message.text.lower())
async def LibraHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(6))
    await bot.send_photo(message.chat.id, open("Data/libra.jpg", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп скорпион' in message.text.lower())
async def ScorpioHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(7))
    await bot.send_photo(message.chat.id, open("Data/scorpio.jpg", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп стрелец' in message.text.lower())
async def SagittariusHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(8))
    await bot.send_photo(message.chat.id, open("Data/sagittarius.png", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп козерог' in message.text.lower())
async def CapricornHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(9))
    await bot.send_photo(message.chat.id, open("Data/capricorn.png", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп водолей' in message.text.lower())
async def AquariusHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(10))
    await bot.send_photo(message.chat.id, open("Data/aquarius.png", 'rb'))


@dp.message_handler(lambda message: message.text and 'гороскоп рыбы' in message.text.lower())
async def PiscesHandler(message: types.Message):
    await message.reply(pars.ParseHoroscope(11))
    await bot.send_photo(message.chat.id, open("Data/pisces.jpg", 'rb'))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
