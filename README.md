# Healthcheck-decorator


The idea is to decorate a function to monitor if it is executed


## How to use

Simply add the decorator to the function you want to monitor

```
from healtcheck_decorator.healthcheck import healthcheck


@healthcheck
def test():
    pass
```

Without any parameters, the decorator adds the function to the monitor using the name of the function itself as a key to save it in the cache.

`@healthcheck(key='TEST-KEY')` 

## Monitor

You can check all the function added to monitor with:

`keys = HealthcheckedFunctionMonitor().get()` 

HealthcheckedFunctionMonitor is a singleton


More info on the implementation here: [healthcheck-decorator-pip-tester](https://github.com/Trafitto/healthcheck-decorator-pip-tester)

## Tests

Before launching the tests you must make sure you have installed the package with: 

`make package_install`

or

`pip install .`

Then you can launch the test:

`make test`

or 


`pytest`