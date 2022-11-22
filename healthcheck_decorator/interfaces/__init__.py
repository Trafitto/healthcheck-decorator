
from .redis import RedisInterface
from .memcached import MemcachedInterface


CACHE_STORAGE_LIST = [
    {'redis': RedisInterface},
    {'memcached', MemcachedInterface}
]