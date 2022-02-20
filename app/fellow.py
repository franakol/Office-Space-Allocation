from app.person import Person

class Fellow(Person):
    """tis is the Fellow class"""

    def __init__(self, name, sex, age):
        super(Fellow, self).__init__(name, sex, age)
        self.wants_accommodation = False

def request_accommodation(self):
    self.wants_accommodation = True