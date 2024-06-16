from .PersonBookInterface import PersonBookInterface
from .PersonBook import PersonBook
import mysql.connector

class PersonBookDAO(PersonBookInterface):
    host = "localhost"
    user = "root"
    password = ""
    database = "Booking"
    @classmethod
    def get_all_bookings(cls):
        db = mysql.connector.connect(
            host=cls.host,
            user=cls.user,
            password=cls.password,
            database=cls.database
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM PersonBook")
        result = cursor.fetchall()
        db.close()
        objs = cls.__convert_db_return_to_objs(result)
        return objs
    @classmethod
    def create_booking(cls, personBook):
        db = mysql.connector.connect(
            host=cls.host,
            user=cls.user,
            password=cls.password,
            database=cls.database
        )
        cursor = db.cursor()
        sql = "INSERT INTO PersonBook (name, email, checkinDate, checkoutDate, roomType, location) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (personBook.name, personBook.email, personBook.checkinDate, personBook.checkoutDate, personBook.roomType, personBook.location)
        cursor.execute(sql, val)
        db.commit()
        db.close()

    @classmethod
    def delete_booking(cls, booking_id):
        db = mysql.connector.connect(
            host=cls.host,
            user=cls.user,
            password=cls.password,
            database=cls.database
        )

        cursor = db.cursor()

        sql = f"DELETE FROM PersonBook WHERE id = {booking_id}"

        cursor.execute(sql)

        db.commit()
        db.close()
    @classmethod
    def get_cursor(cls):
        db = mysql.connector.connect (
            host = cls.host,
            user = cls.user,
            password = cls.password,
            database = cls.database
        )

        cursor = db.cursor()
        return cursor

    @classmethod
    def __convert_db_return_to_obj(cls, singleResult):
        id = singleResult[0]
        name = singleResult[1]
        email = singleResult[2]
        checkinDate = singleResult[3]
        checkoutDate = singleResult[4]
        roomType = singleResult[5]
        location = singleResult[6]
        return PersonBook(id=id, name=name, email=email, checkinDate=checkinDate, checkoutDate=checkoutDate, roomType=roomType, location=location)
    @classmethod
    def __convert_db_return_to_objs(cls, result):
        return [cls.__convert_db_return_to_obj(singleResult) for singleResult in result]

