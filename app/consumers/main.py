from faststream import FastStream
from faststream.kafka.broker import KafkaBroker
from settings.config import get_settings
from consumers.handlers import router


settings = get_settings()


def get_app() -> FastStream:
    broker = KafkaBroker(settings.kafka_broker_url)
    broker.include_router(router=router)
    app = FastStream(broker=broker)
    return app
