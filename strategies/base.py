from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class UnaryOperation(ABC):
    @abstractmethod
    def execute(self, a):
        pass
