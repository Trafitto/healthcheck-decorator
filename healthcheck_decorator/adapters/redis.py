from .base_adapter import BaseCacheAdapter


class RedisAdapter(BaseCacheAdapter):

    def __init__(self, client):
        self.client = client

    def get(self, key: str):
        return self.client.get(key)

    def set(self, key: str, value: str, ttl: int):
        self.client.set(key, value, ttl)
