from .base_interface import BaseCacheInterface


class MemcachedInterface(BaseCacheInterface):

    def __init__(self):
        pass

    def get(self, key: str):
        return self.client.get(key)

    def set(self, key: str, value: str, ttl: int):
        self.client.set(key, value, ttl)
