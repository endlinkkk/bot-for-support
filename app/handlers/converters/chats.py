from ddtos.messages import ChatItemDTO, ChatListenerDTO


def convert_chats_dtos_to_message(chats: list[ChatItemDTO]) -> str:
    return "\n\n".join(
        (
            "Список всех доступных чатов: ",
            "\n".join(
                f"OID: <code>{chat.oid}</code>\nПроблема:{chat.title}\n"
                for chat in chats
            ),
        )
    )


def convert_chat_listener_response_to_listener_dto(
    listener_data: dict,
) -> ChatListenerDTO:
    return ChatListenerDTO(oid=listener_data["oid"])
