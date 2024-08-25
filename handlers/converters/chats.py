from ddtos.messages import ChatItemDTO


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