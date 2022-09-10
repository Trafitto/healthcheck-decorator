import functools
import redis
from .monitor import HealthcheckedFunctionMonitor


monitor = HealthcheckedFunctionMonitor()
redis_client = redis.Redis(host='redis', port=6379, db=0)
default_ttl = 24 * 60 * 60 * 1000

def healthcheck(func=None, key=None, ttl=default_ttl, cache_instance=redis_client):
    if func is None:
        return functools.partial(healthcheck, key=key, ttl=ttl, cache_instance=cache_instance)
    cache_key = key or func.__name__
    monitor.set(cache_key)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        cache_instance.set(cache_key, 'updated', ttl)
        return result

    return wrapper
