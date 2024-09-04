from faststream import Context
from faststream.kafka import KafkaRouter
from consumers.schemas import NewChatMessageSchema
from containers.factories import get_container
from services.web import BaseChatWebService
from settings.config import get_settings

from aiogram import Bot


settings = get_settings()
router = KafkaRouter()


@router.subscriber(settings.new_message_topic, group_id=settings.kafka_group_id)
async def new_message_subcription_handler(
    message: NewChatMessageSchema, key: bytes = Context("message.raw_message.key")
):
    container = get_container()
    async with container() as request_container:
        service: BaseChatWebService = await request_container.get(BaseChatWebService)
        listeners = await service.get_chat_listeners(chat_oid=key.decode())
        chat_info = await service.get_chat_info(chat_oid=key.decode())
        bot: Bot = await request_container.get(Bot)

        for listener in listeners:
            await bot.send_message(
                chat_id=listener.oid,
                text=f"Chat: {chat_info.title}\nMessage: \n{message.message_text}",
            )


# Exception: ('string', 'scdcscdc', 'ss') raise Exception(listener.oid, chat_info.title, message.message_text)
