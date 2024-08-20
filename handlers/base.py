from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from containers.factories import get_container
from settings.config import Settings


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    container = get_container()
    settings = await container.get(Settings)
    await message.answer(text=settings.greeting_text)
