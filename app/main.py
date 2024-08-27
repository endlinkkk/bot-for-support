import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from handlers.base import router as base_router
from handlers.chats import router as chat_router
from settings.config import get_settings


dp = Dispatcher()


def my_commands() -> list[BotCommand]:
    return [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="chats", description="Показать все чаты"),
        BotCommand(command="set_chat", description="Установить чат"),
    ]


async def main() -> None:
    app = get_app()
    await app.set_my_commands(my_commands())
    dp.include_router(base_router)
    dp.include_router(chat_router)
    await dp.start_polling(app)


def get_app() -> Bot:
    settings = get_settings()
    bot = Bot(
        token=settings.api_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    return bot


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
