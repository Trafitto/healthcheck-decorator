import redis
from .conf import REDIS_HOST, REDIS_DB, REDIS_PORT
from .conf import CACHE_STORAGE

class HealthcheckedFunctionMonitor:
    healthchecked_function = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(
                HealthcheckedFunctionMonitor, cls).__new__(cls)
        return cls.instance

    def set(self, key):
        self.healthchecked_function.append(key)

    def get(self):
        return self.healthchecked_function

    def delete(self, key):
        if key == '*':
            self.healthchecked_function = []
        if self.healthchecked_function:
            del self.healthchecked_function[key]
