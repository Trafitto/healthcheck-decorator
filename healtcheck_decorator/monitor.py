import redis
from .conf import REDIS_HOST, REDIS_DB, REDIS_PORT


class HealthcheckedFunctionMonitor:
    healchecked_function = []
    cache = None

    def __init__(self):
        self.cache = self.get_cache_instance()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(
                HealthcheckedFunctionMonitor, cls).__new__(cls)
        return cls.instance

    def set(self, key):
        self.healchecked_function.append(key)

    def get(self):
        return self.healchecked_function

    def get_cache_instance(self):
        if not self.cache:
            self.cache = redis.Redis(
                host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        return self.cache
