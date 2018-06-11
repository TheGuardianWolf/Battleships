from abc import ABC, abstractmethod


class Adapter(ABC):
    @abstractmethod
    def get_grid(self, prompt):
        pass

    @abstractmethod
    def get_bool(self, prompt):
        pass
