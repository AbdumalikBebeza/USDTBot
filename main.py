from aiogram.utils import executor
from aiogram import types
from config import bot, dispatcher, ADMINS
from parser import parser
import logging

curs = 0
comsa = 0


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer("чтобы поменять курс и комсу надо ввести\n"
                             "/set курс комса (пробел обязательно)")
    else:
        await message.reply(
            "Привет! Я бот для отслеживания цены Litecoin. Используйте команду "
            "/price, чтобы получить текущую цену Litecoin, или отправьте мне количество Litecoin для конвертации в USD.")


@dispatcher.message_handler(commands=['set'])
async def set_comsa_and_curs(message: types.Message):
    try:
        if message.from_user.id in ADMINS:
            mess = message.text.split()
            global curs, comsa
            curs = int(mess[1])
            comsa = int(mess[2])
            await message.answer("курс и комса поменялись")

    except IndexError:
        await message.answer("Проверьте правильность написания курса и комсы")


@dispatcher.message_handler(commands=['price'])
async def get_litecoin_price(message: types.Message):
    usdt_price = parser()
    if usdt_price is not None and usdt_price[0] == '$':
        await message.reply(f"Текущая цена USDT.: ${usdt_price[1]}")
    else:
        await message.reply("Не удалось получить цену Litecoin. Пожалуйста, попробуйте позже.")


@dispatcher.message_handler()
async def convert_to_usd(message: types.Message):
    try:
        usdt_amount = float(message.text)
        usdt_price = parser()
        if usdt_price is not None and usdt_price[0] == '$':
            usd_value = int(usdt_amount * float(usdt_price[1]) * curs) + comsa
            await message.reply(f"{usd_value:,}")
        else:
            await message.reply("Не удалось получить цену USDT. Пожалуйста, попробуйте снова позже.")
    except ValueError:
        await message.reply("Неверный ввод. Пожалуйста, введите правильное количество Litecoin.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dispatcher, skip_updates=True)
