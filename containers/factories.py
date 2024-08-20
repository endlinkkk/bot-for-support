from functools import lru_cache
from dishka import AsyncContainer, make_async_container

from containers.providers import MyProvider


@lru_cache(1)
def get_container() -> AsyncContainer:
    return make_async_container(
        MyProvider(),
    )
