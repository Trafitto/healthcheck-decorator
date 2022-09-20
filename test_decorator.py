
import pytest
from healthcheck_decorator.healthcheck import healthcheck
from healthcheck_decorator.monitor import HealthcheckedFunctionMonitor


@pytest.fixture(autouse=True)
def redis_db():
    monitor = HealthcheckedFunctionMonitor()
    cache = monitor.get_cache_client()
    keys = cache.keys('*')
    monitor.delete('*')
    if keys:
        cache.delete(*keys)


def test_add_function_to_monitor():
    @healthcheck(key='test_function')
    def to_be_decorated():
        keys = HealthcheckedFunctionMonitor().get()
        assert len(keys) == 1
        assert keys[0] == 'test_function'
    to_be_decorated()


def test_cache_key():
    @healthcheck()
    def to_be_decorated():
        print('done')
    to_be_decorated()
    monitor = HealthcheckedFunctionMonitor()
    keys = monitor.get()
    redis = monitor.get_cache_client()
    redis_key = redis.keys('*')
    assert len(keys) == len(redis_key)
    assert redis_key[0].decode('ascii') == 'to_be_decorated'
    assert redis.get(redis_key[0]).decode('ascii') == 'updated'
