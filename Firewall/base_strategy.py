from abc import ABC, abstractmethod

class FirewallStrategy(ABC):
    @abstractmethod
    def filter(self, packet: dict) -> bool:
        pass
