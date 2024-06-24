from abc import ABC, abstractmethod

class SequenceBase(ABC):
    @abstractmethod
    def append(self):
        return

    @abstractmethod
    def iter_delete(cls, name, email, checkinDate, checkoutDate, roomType, location):
        pass

    @abstractmethod
    def to_list(self):
        pass

    @abstractmethod
    def length(self):
        pass