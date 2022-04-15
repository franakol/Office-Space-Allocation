class Person(object):
    """represents someone within the Dojo"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.is_allocated = False
        self.office_name = None
        self.type_ = self.__class__.__name__
        self.name = self.first_name + ' ' + self.last_name


class Fellow(Person):
    def __init__(self, first_name, last_name, wants_accommodation=False):
        super(Fellow, self).__init__(first_name, last_name)
        self.wants_accommodation = wants_accommodation
        self.livingspace_name = None


class Staff(Person):
    def __init__(self, first_name, last_name):
        super(Staff, self).__init__(first_name, last_name)
