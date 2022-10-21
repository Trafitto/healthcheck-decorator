
from .redis import RedisAdapter
from .memcached import MemcachedAdapter


CACHE_STORAGE_LIST = [
    {'redis': RedisAdapter},
    {'memcached', MemcachedAdapter}
]