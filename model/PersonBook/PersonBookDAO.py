from .PersonBookInterface import PersonBookInterface
from .PersonBook import PersonBook
from sequences.linkedlist import LinkedList
class PersonBookDAO(PersonBookInterface):
    sequence = LinkedList()

    @classmethod
    def get_all_bookings(cls):
        return cls.sequence.to_list()
    @classmethod
    def create_booking(cls, personBook):
        personBook.id = cls.sequence.length()
        cls.sequence.append(personBook)

    @classmethod
    def delete_booking(cls, booking_id):
        def isSameTarget(personBook):
            return personBook.id == booking_id
        cls.sequence.iter_delete(isSameTarget)


