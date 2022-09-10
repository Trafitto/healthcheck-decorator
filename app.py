from healthcheck-decorator.healthcheck import healthcheck


@healthcheck
def test():
    print('OLA')
