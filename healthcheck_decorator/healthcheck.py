import functools
from .monitor import HealthcheckedFunctionMonitor
from .conf import CACHE_STORAGE

monitor = HealthcheckedFunctionMonitor()


def healthcheck(func=None, key=None, ttl=None):
    cache_client = CACHE_STORAGE.instance
    if ttl is None:
        ttl=cache_client.default_ttl

    if func is None:
        return functools.partial(healthcheck, key=key, ttl=ttl)
    cache_key = key or func.__name__
    monitor.set(cache_key)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        cache_client.set(key=cache_key, value='updated', ttl=ttl)
        return result

    return wrapper
