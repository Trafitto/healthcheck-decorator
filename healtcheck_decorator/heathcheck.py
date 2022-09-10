import functools


def healthcheck(func=None, key=None, ttl=9000, cached_table='REDIS INSTANCE'):
    if func is None:
        return functools.partial(healthcheck, key=key, ttl=ttl, cached_table=cached_table)
    
    cache_key = key or func.__name__
    print(f'Load function with key: {cache_key}')
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # cached_table.set(cache_key, "updated", ttl)
        print(cache_key)
        return result

    return wrapper
