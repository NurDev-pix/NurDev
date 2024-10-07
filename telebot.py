import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode

# Токен вашего бота
API_TOKEN = '7807837081:AAG4XlBm2pQHAZAIiI_PvHwH53RF8Nq77_M'

# Идентификаторы группы и вашего аккаунта
GROUP_CHAT_ID = '-1002415168682'
YOUR_USER_ID = '7318042041'

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обрабатываем сообщения от вас
@dp.message_handler(lambda message: message.from_user.id == int(YOUR_USER_ID))
async def forward_to_group(message: types.Message):
    try:
        # Пересылаем сообщение в группу
        await bot.forward_message(chat_id=GROUP_CHAT_ID, from_chat_id=message.from_user.id, message_id=message.message_id)
    except Exception as e:
        await message.reply(f"Не удалось переслать сообщение в группу: {e}")

# Обрабатываем сообщения от других пользователей
@dp.message_handler(lambda message: message.from_user.id != int(YOUR_USER_ID))
async def forward_to_you(message: types.Message):
    try:
        # Пересылаем сообщение вам
        await bot.forward_message(chat_id=YOUR_USER_ID, from_chat_id=message.from_user.id, message_id=message.message_id)
    except Exception as e:
        await bot.send_message(YOUR_USER_ID, f"Не удалось переслать сообщение от {message.from_user.username}: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)