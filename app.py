import time
from healthcheck_decorator.healthcheck import healthcheck
from healthcheck_decorator.monitor import HealthcheckedFunctionMonitor
from healthcheck_decorator.conf import CACHE_STORAGE
import redis

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0
redis_client = redis.Redis(
                host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
cache = CACHE_STORAGE().set_client(redis_client)

@healthcheck
def test():
    print('This is test function')

@healthcheck(key='TEST-KEY')
def test_key():
    print('This is test function with key name on decorator')

@healthcheck
def test_function_not_working():
    print('This function never runs')

def checker():
    monitor = HealthcheckedFunctionMonitor()
    keys = monitor.get()
    cache_client = redis_client
    for key in keys:
        if cache_client.get(key):
            print(f'{key} ok')
        else:
            print(f'{key} not working')

if __name__ == '__main__':
    test()
    time.sleep(1)
    test_key()
    time.sleep(1)
    checker()
    while True:
        pass
    