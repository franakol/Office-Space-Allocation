class Room():
    """the base model for a room in the Dojo"""

    def __init__(self, name):
        """
        self is a reference to the current instance of the class
        used to access variables that belong to the class
        """
        self.name = name
        self.members = []
        self.max_capacity = 0
        self.type_ = self.__class__.__name__

    def is_empty(self):
        return len(self.members) == 0

    def is_full(self):
        return len(self.members) >= self.max_capacity

    def __repr__(self):
        template = "Room Name: \"{}\" Type: \"{}\"\n----------------------------------------\n{}\n\n"
        return template.format(self.name, self.type_,
        ", ".join([member.name for member in self.members]) if len(
                                self.members) != 0 else "<-- No Members-->")


class Office(Room):
    """this is a model for an office within the Dojo"""

    def __init__(self, name):
        super(Office, self).__init__(name)
        self.max_capacity = 6


class LivingSpace(Room):
    """"this is a model for a living sppace found in the Dojo"""

    def __init__(self, name):
        super(LivingSpace, self).__init__(name)
        self.max_capacity = 4
