class Monitor:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Monitor, cls).__new__(cls)
        return cls.instance

    def __init__(self, cache):
        self.cache = cache
        self.healchecked_function = []

    def set(self, key):
        self.healchecked_function.append(key)

    def get(self):
        return self.healchecked_function
