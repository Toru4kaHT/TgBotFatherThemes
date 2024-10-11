import logging
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from config import settings
from create_bot import bot, dp
from handlers.user_router import user_router
from handlers.admin_router import admin_router
from create_bot import set_commands
from aiogram.types import BotCommand, BotCommandScopeDefault
from create_bot import admins
# from work_time.time_func import send_time_msg



# Функция для создания меню комманд
async def set_commands():
    # Создаем список команд, которые будут доступны пользователям
    commands = [BotCommand(command='start', description='Старт')]
    # Устанавливаем эти команды как дефолтные для всех пользователей
    await bot.set_my_commands(commands, BotCommandScopeDefault())


# Стартовая функция бота
async def on_startup():
    # Обновляем список комманд
    await set_commands() 
    # Указывает url к веб хукам
    await bot.set_webhook(f'{settings.BASE_URL}{settings.WEBHOOK_PATH}') 
    # Отправляем сообщение админам, что бот запущен
    for admin in admins:
        await bot.send_message(chat_id=admin, text='Бот запущен 🧩')

async def on_shutdown():
    # Отправляем сообщение админам, что бот остановлен
    for admin in admins:
        await bot.send_message(chat_id=admin, text='Бот остановлен 😧')
    # Удаляем вебхуки и очещаем ожидающие обновления
    await bot.delete_webhook(drop_pending_updates=True) 
    # Закрываем сессию бота
    await bot.session.close() 


# Главная функция для запуска бота
# Основная функция, которая запускает приложение
def main() -> None:
    # Подключаем маршрутизаторы (роутер) для обработки сообщений
    dp.include_router(user_router)
    dp.include_router(admin_router)

    # Регистрируем функцию, которая будет вызвана при старте бота
    dp.startup.register(on_startup)

    # Регистрируем функцию, которая будет вызвана при остановке бота
    dp.shutdown.register(on_shutdown)

    # Создаем веб-приложение на базе aiohttp
    app = web.Application()

    # Настраиваем обработчик запросов для работы с вебхуком
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,  # Передаем диспетчер
        bot=bot  # Передаем объект бота
    )
    # Регистрируем обработчик запросов на определенном пути
    webhook_requests_handler.register(app, path=settings.WEBHOOK_PATH)

    # Настраиваем приложение и связываем его с диспетчером и ботом
    setup_application(app, dp, bot=bot)

    # Запускаем веб-сервер на указанном хосте и порте
    web.run_app(app, host=settings.HOST, port=settings.PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    main()