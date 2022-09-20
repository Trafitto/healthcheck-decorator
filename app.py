import time
from healtcheck_decorator.heathcheck import healthcheck
from healtcheck_decorator.monitor import HealthcheckedFunctionMonitor


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
    cache_client = monitor.get_cache_client()
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
    