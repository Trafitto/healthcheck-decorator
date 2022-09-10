from healtcheck_decorator.heathcheck import healthcheck
import time

@healthcheck
def test():
    print('This is test function')

@healthcheck(key='TEST-KEY')
def test_key():
    print('This is test function with key name on decorator')


if __name__ == '__main__':
    while True:
        pass
    