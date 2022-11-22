
import pytest
import redis
from healthcheck_decorator.healthcheck import healthcheck
from healthcheck_decorator.monitor import HealthcheckedFunctionMonitor
from healthcheck_decorator.conf import CACHE_STORAGE

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

@pytest.fixture(autouse=True)
def redis_db():
    monitor = HealthcheckedFunctionMonitor()
    cache = redis_client
    keys = cache.keys('*')
    monitor.delete('*')
    if keys:
        cache.delete(*keys)


def test_add_function_to_monitor():
    CACHE_STORAGE().set_client(redis_client)
    @healthcheck(key='test_function')
    def to_be_decorated():
        keys = HealthcheckedFunctionMonitor().get()
        assert len(keys) == 1
        assert keys[0] == 'test_function'
    to_be_decorated()


def test_cache_key():
    CACHE_STORAGE().set_client(redis_client)
    @healthcheck()
    def to_be_decorated():
        print('done')
    to_be_decorated()
    monitor = HealthcheckedFunctionMonitor()
    keys = monitor.get()
    redis = redis_client
    redis_key = redis.keys('*')
    assert len(keys) == len(redis_key)
    assert redis_key[0].decode('ascii') == 'to_be_decorated'
    assert redis.get(redis_key[0]).decode('ascii') == 'updated'
