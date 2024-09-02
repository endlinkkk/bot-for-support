from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ErrorEvent
from aiogram import F
from aiogram.filters import ExceptionTypeFilter
from exceptions.base import ApplicationException
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

    container = get_container()
    async with container() as request_container:
        chat_oid = command.args
        service: BaseChatWebService = await request_container.get(BaseChatWebService)
        await service.add_listener(
            telegram_chat_id=message.chat.id, chat_oid=chat_oid
        )

        await message.answer(text=f"Successfully listening to the chat: {chat_oid}")


@router.error(ExceptionTypeFilter(ApplicationException), F.update.message.as_("message"))
async def handle_my_custom_exception(event: ErrorEvent, message: Message):
    await message.answer(f"Oops, something went wrong!\n{event.exception.message}()")





@router.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
