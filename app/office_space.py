from app.room import Room

class Office_space(Room):
    """this is class Office_space"""

def __init__(self, name):
    super(Office_space, self).__init__(name)
    self.max_capacity = 6
    self.populate_slots()

def populate_slots(self):
    for i in range(0, self.max_capacity):
        self.room_mates.append('X')