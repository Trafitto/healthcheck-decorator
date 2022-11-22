from abc import ABC, abstractmethod

class BaseCacheInterface(ABC):
    client = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(
                BaseCacheInterface, cls).__new__(cls)
        return cls.instance

    def set_client(self, client):
        self.client = client

    @property
    def default_ttl(self):
        return 24 * 60 * 60 * 1000
    
    @abstractmethod
    def get(self, key:str):
        pass

    @abstractmethod
    def set(self, key:str, value:str, ttl:int):
        pass
