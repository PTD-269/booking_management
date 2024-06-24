class PersonBook:
    tableName = "PersonBook"
    def __init__(self, name, email, checkinDate, checkoutDate, roomType, location, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.checkinDate = checkinDate
        self.checkoutDate = checkoutDate
        self.roomType = roomType
        self.location = location