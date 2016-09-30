class Student:
    def __init__(self, studentDict):
        self.name = studentDict['nm']
        self.address = studentDict['addr']
        self.city = studentDict['city']
        self.pincode = studentDict['pin']
