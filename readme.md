# Tg bot for support service

service: https://github.com/endlinkkk/fastapi-ddd-kafka-example

Use case:
- The support agent logs into the bot and selects an active chat from the list
- The bot remembers which chat the agent is writing to and allows sending messages to the active chat
- The client immediately receives messages sent by the agent via the bot (With the help of Kafka Consumer)
- When a customer closes the chat, the support agent receives a notification