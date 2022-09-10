import time
import redis
from healtcheck_decorator.heathcheck import healthcheck
from healtcheck_decorator.monitor import HealthcheckedFunctionMonitor

redis_client = redis.Redis(host='redis', port=6379, db=0)

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
    keys = HealthcheckedFunctionMonitor().get()
    for key in keys:
        if redis_client.get(key):
            print(f'{key} ok')
        else:
            print(f'{key} not working')

if __name__ == '__main__':
    '''     test()
    time.sleep(1)
    test_key()
    time.sleep(1)
    checker() '''
    while True:
        pass
    