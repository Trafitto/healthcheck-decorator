from abc import ABC, abstractmethod


class BaseCacheInterface(ABC):
    
    @abstractmethod
    def get(self, key:str):
        pass

    @abstractmethod
    def set(self, key:str, value:str, ttl:int):
        pass
