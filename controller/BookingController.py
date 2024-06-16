from model.PersonBook.PersonBook import PersonBook
from model.PersonBook.PersonBookDAO import PersonBookDAO

class BookingController:
    @staticmethod
    def get_all_bookings():
        personBooks = PersonBookDAO.get_all_bookings()
        return [p.__dict__ for p in personBooks]

    @staticmethod
    def create_booking(name, email, checkinDate, checkoutDate, roomType, location):
        personBook = PersonBook(name=name, email=email, checkinDate=checkinDate, checkoutDate=checkoutDate, roomType=roomType, location=location)
        PersonBookDAO.create_booking(personBook)
        print("Added")

    @staticmethod
    def delete_booking(booking_id):
        PersonBookDAO.delete_booking(booking_id)
        print("Deleted")
