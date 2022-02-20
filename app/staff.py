from app.person import Person

class Staff(Person):
    """this is the Staff class"""

    def __init__(self, name, sex, age):
        super(Staff, self).__init__(name,sex, age)