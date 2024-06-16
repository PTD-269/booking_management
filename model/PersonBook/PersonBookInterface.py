from abc import ABC, abstractmethod

class PersonBookInterface(ABC):
    @classmethod
    @abstractmethod
    def get_all_bookings(cls):
        return

    @classmethod
    @abstractmethod
    def create_booking(cls, name, email, checkinDate, checkoutDate, roomType, location):
        pass

    @classmethod
    @abstractmethod
    def delete_booking(cls, booking_id):
        pass
