class Room:
    def __init__(self, name):   
        """
        self is a reference to the current instance of the class
        used to access variables that belong to the class
        """
    self.name = name   
    self.max_capacity = 0

class Office(Room):
    """representing an office within the dojo"""

    def __init__(self, name):
        