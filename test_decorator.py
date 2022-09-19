
import pytest
from healtcheck_decorator.heathcheck import healthcheck
from healtcheck_decorator.monitor import HealthcheckedFunctionMonitor



@pytest.fixture(autouse=True)
def redis_db():
    #TODO Clear cache after test
    pass

def test_add_function_to_monitor():
    @healthcheck(key='test_function')
    def to_be_decorated():
        keys = HealthcheckedFunctionMonitor().get()
        print(keys)
        assert len(keys) == 1
        assert keys[0] == 'test_function'
    to_be_decorated()


