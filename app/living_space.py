from app.room import Room

class Living_space(Room):
    """this is class Living_space"""

    def __init__(self, name):
        super(Living_space, self).__init__(name)
        self.max_capacity = 4
        self.populate_slots()

    def populate_slots(self):
        for i in range(0, self.max_capacity):
            self.room_mates.append('X')