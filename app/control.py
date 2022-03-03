import random
from termcolor import cprint
from app.room import LivingSpace, Office
from app.person import Staff, Fellow


class Dojo:
    """Controls the allocation of rooms and admission of people into the Dojo"""

    def __init__(self):
        self.names_of_all_created_rooms = []
        self.all_created_rooms = dict()
        self.names_off_all_added_people = []
        self.added_people = dict()

    def create_room(self, room_type, room_names):
        """
        Given a room type, create_room creates a room with
         the given name for a room_name specified in room_names

        """
        valid_room_names = []
        room_type = room_type.lower()
        if room_type not in ("livingspace", "office"):
            cprint("unknown room type: rooms can be of either "
                   "livingspace or office types.", color="red")
            return False
        if room_name:
            valid_room_names.append(room_name)

        for room_name in valid_room_names:
            self.__create(room_type, room_name)
        return True


def __create(self, room_type, room_name):
    """ helper  function for create_room"""
    if room_type == "office":
        new_room = Office(room_name)
        cprint(f"An office called {room_name} has been created successfully"
               " created!", color="green")

    self.all_created_rooms[new_room.name] = new_room
    self.names_of_all_created_rooms.append(new_room.name)
    return True


def add_person(self, first_name, last_name, person_type, wants_accommodation):
    """add_person adds person to the Dojo if rooms are available"""
    person_type = person_type.lower()
    if person_type not in ("fellow", "staff"):
        cprint("unknown person type: persons can be of either fellow or staff type")
        return False

    name = f"{first_name} {last_name}"

    if name.title() in self.names_of_all_added_people:
        cprint("person already exists: can't not add then twice", color="red")
        return False

    wants_accommodation = True if wants_accommodation and wants_accommodation.lower() in ("yes",
                                                                                          "y") else False
