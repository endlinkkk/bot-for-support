from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from containers.factories import get_container
from handlers.converters.chats import convert_chats_dtos_to_message
from services.web import BaseChatWebService


router = Router()


@router.message(Command("chats"))
async def get_all_chats_handler(message: Message) -> None:
    """
    This handler receives messages with `/chats` command
    """
    container = get_container()

    async with container() as request_container:
        service: BaseChatWebService = await request_container.get(BaseChatWebService)
        chats = await service.get_all_chats()

        await message.answer(text=convert_chats_dtos_to_message(chats))


@router.message(Command("set_chat"))
async def set_chat_handler(message: Message, command: CommandObject) -> None:
    """
    This handler receives messages with `/set-chat` command
    """

    await message.answer(text=f"{command.args}")


@router.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
