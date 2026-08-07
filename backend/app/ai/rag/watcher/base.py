from abc import ABC, abstractmethod


class BaseWatcher(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
