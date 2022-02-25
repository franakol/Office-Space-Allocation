import random   
import os
from  app.living_space import living_space 
from app.office_space import office_space
from app.fellow import Fellow
from app.staff import Staff
"""from app.models.database import, Person, room"""


class Dojo(object):
    """
    Class Dojo to create rooms, add rooms, define the room types  and add people to the rooms to
    
"""
"""DATABASE_VAL = None"""

def __init__(self, id, name):
    self.id = id
    if isinstance(name, str):
        self.name = name
        else:
            raise TypeError

        self.fellow = {}
        self.staff = {}
        self.living_space = {}
        self.office_space = {}
        self.available_living_slots ={}  
        self.available_office_slots = {}
        self.allocated_spots = {}
        self.unallocated_people = []
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.database = Database(self.DATABASE_VAL)

def create_room(self, room_type, rooms):
    room_available = False
    if instance(rooms, list):
        space =room_type.title()
        if (not space == 'Office') and (not sapace == 'Living'):
            print("Room type not recognized")
        for room_name in rooms: # Loops through rooms arguments for all rooms in the list
            if space == 'Office':
                if self.check_if_room_exists(room_name, space) is True:
                    print("Room with name " +
                    room_name + " already exists!")
                    continue
                else:
                    current_room = office_space(room_name)
                    self.office_spaces[room_name] = current_room
                    print("An Office Called " + current_room_name.name +
                                " has beeen successfully created!")
                    room_available = True

                else:
                    if self.check_if_room_exists(room_name, space) is True:
                    print("Room with name " +
                            room_name + "Already Exists!")
                    continue
                else:
                    current_room =living_space(room_name)
                    self.living_spaces[room_name] = current_room
                    print("A Living Space Called " + current_room.name +
                              " has been successfully created!")
                    room_available = True

                else:
                    raise ValueError('Rooms arguments should be a list')
                if room_available == True:
                    person_type = ''
                    for person in self.unallocated_people:
                        if isinstance(person, Fellow):
                            person_type = 'Fellow'
                            person_source = self.fellows
                            wants_accommodation = True
                        elif isinstance(person, Staff):
                            person_type = 'Staff'
                            person_source = self.staff
                            wants_accommodation = False
                        print('\nNOTE::\n{}'.format(person.name) +
                                 ' seems to have no room yet')
                        self.add_person(person.name, person_type, wants_accommodation)
                        Self.unallocated_people.remove(person)

def add_person(self, person_name, person_type, wants_accommodation):
    """this functions adds person to the dojo and and allocates a room to them"""   
    sex = 'Male' # TODO: Configure sex argument
    age = 25 # TODO: Configure Sex
    person_type = person_type.title()

    if not ((person_type == 'Fellow') or (person_type == 'Staff')):
        import pdb
        pdb.set_trace()
    else:
        if self.check_if_person_exists(person_name, person_type) is True:
            print("Person Exists!")
            return
    else:
        if person_type == 'Fellow':
            fellow = Fellow(person_name, sex, age)
            if wants_accommodation is True:
                fellow.request_accommodation()
                self.fellows[person_name] = Fellow
            elif person_type == 'staff':
                staff = Staff(person_name, sex, age)
                self.staff[person_name] = staff
                print(person_name + ' has been successfully added\n\n')

                self.add_to_room(person_name, person_type)
                print('Living space available')
                print(self.available_living_slots)
                print('office spaces available')
                print(self.available_office_slots)

def check_if_person_exists(self, person, person_type)
   """this function checks if the person has already been added"""
   if person_type == 'Fellow':
       person_source = self.Fellows
    elif person_type == 'Staff':
        person_source = self.Staff

    if person in person_source:
        if person_source[person] in self.unallocated_people:
              return False
        else:
            return True
        else:
            return False

def check_if_room_exists(self, room, room_type):
    """this function checks if the room has already been added"""
    if room_type == 'Living':
        space = self.living_spaces
    elif room_type == 'office':
        space = self.office_spaces

    if room in space:
        return True
    else:
        return False

def add_to_room(self, person, person_type):
    allocated = False
    person_source = []
    if person_type == 'Fellow':
        self.find_empty_slots('Living')
        if self.fellows[person].wants_accommodation is True:
            living_allocated = False
            while (living_allocated is False) and len(self.available_living_slots) > 0:
                random_value = random.choice(list)