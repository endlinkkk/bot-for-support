import asyncio
from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ErrorEvent, ReplyKeyboardRemove
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.filters import ExceptionTypeFilter
from keyboards.reply import keyboard
from exceptions.base import ApplicationException
from containers.factories import get_container
from handlers.converters.chats import convert_chats_dtos_to_message
from services.web import BaseChatWebService
from aiogram.fsm.state import State, StatesGroup



router = Router()


class ChatStates(StatesGroup):
    listening = State()


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
async def set_chat_handler(
    message: Message, command: CommandObject, state: FSMContext
) -> None:
    if not command.args:
        await message.answer("Please provide a chat OID. Usage: /set_chat chat_oid")
        return

    container = get_container()
    async with container() as request_container:
        chat_oid = command.args
        service: BaseChatWebService = await request_container.get(BaseChatWebService)

        try:
            await service.add_listener(
                telegram_chat_id=message.chat.id, chat_oid=chat_oid
            )
        except Exception as e:
            await message.answer(f"Error setting up chat listener: {str(e)}")
            return

        await state.update_data(chat_oid=chat_oid)
        # TODO Сделать кнопку выйти и удалить чат (при удалении чата все слушатели должны покинуть чат)

        await message.answer("Вы в чате. Чтобы выйти, нажмите кнопку.", reply_markup=keyboard)
        await state.set_state(ChatStates.listening)


@router.message(ChatStates.listening)
async def handle_listening_messages(message: Message, state: FSMContext):
    user_data = await state.get_data()
    chat_oid = user_data.get('chat_oid')

    container = get_container()
    async with container() as request_container:
        service: BaseChatWebService = await request_container.get(BaseChatWebService)

        if message.text == 'exit':
            await service.delete_listener(telegram_chat_id=message.chat.id, chat_oid=chat_oid)
            await message.answer(f"Вы вышли из чата: {chat_oid}", reply_markup=ReplyKeyboardRemove())


            await state.clear()
        else:
            await service.send_message_to_chat(chat_oid=chat_oid, message=message.text)
            await message.answer(f"Message sent in chat: {chat_oid}\nMessage text: {message.text}")
            await asyncio.sleep(0.5)
            try:
                await message.delete()
            except Exception:
                pass
            


@router.error(
    ExceptionTypeFilter(ApplicationException), F.update.message.as_("message")
)
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
