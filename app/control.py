import os
import random
import pdb
#from turtle import color

from termcolor import cprint

from app.person import Fellow, Person, Staff
from app.room import LivingSpace, Office
from app.database.database import *




class Dojo:
    """Controls the allocation of rooms and admission of people into the Dojo"""

    def __init__(self):
        self.names_of_all_created_rooms = []
        self.all_created_rooms = dict()
        self.names_of_all_added_people = []
        self.added_people = dict()
        self.available_offices = []
        self.available_livingspaces = []
        

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

        for room_name in room_names:
            room_name = room_name.lower()
            if room_name in self.names_of_all_created_rooms:
                cprint(f"a room with name '{room_name}' already exists: please use a different name",
                    color="red")
                return False
            if room_name:
                valid_room_names.append(room_name)

        for room_name in valid_room_names:
            self.__create(room_type, room_name)
        return True

    def __create(self, room_type, room_name):
        """ helper function for create_room """
        if room_type == "office":
            new_room = Office(room_name)
            self.available_offices.append(new_room)
            
            
            cprint(f"An office called {room_name} has been successfully"
                " created!", color="green")

            self.all_created_rooms[new_room.name] = new_room
            self.names_of_all_created_rooms.append(new_room.name)
            return True
        if room_type == "livingspace":
            new_room = LivingSpace(room_name)
            self.available_livingspaces.append(new_room)
            cprint(f"A livingspace called {room_name} has been successfully"
                " created!", color="green")

        self.all_created_rooms[new_room.name] = new_room
        self.names_of_all_created_rooms.append(new_room.name)
        return True

    

    def add_person(self, first_name, last_name, person_type, wants_accommodation):
        """ add_person adds a person to the Dojo. If rooms are available,
        it allocates the person a room according to their type"""
    
        person_type = person_type.lower()
        if person_type not in ("fellow", "staff"):
            cprint("unknown person type: persons can be of either fellow or staff type")
            return False

        name = f"{first_name} {last_name}"

        if name.lower() in self.names_of_all_added_people:
            cprint("person already exists: can't add them twice", color="red")
            return False

        wants_accommodation = True if wants_accommodation and wants_accommodation.lower() in ("yes", "y") else False

        if wants_accommodation and person_type == "staff":
            cprint("staff members cannot be accommodated at the Dojo's livingspaces", color="red")
            return False

        is_added = False
        #if person_type.upper() == "STAFF":
        person = Staff(first_name, last_name)
        cprint(f"{first_name, last_name} has been added successfully", color="blue")
        self.added_people[first_name, last_name] = person
        is_added = True
        self.names_of_all_added_people.append(person.name)
        if len(self.available_offices) != 0:
            office = random.choice(self.available_offices)
            cprint(f"{first_name.lower()} has been allocated office {office.name}", color="green")
            office.members.append(person)
            if office.is_full():
                officeindex = self.available_offices.index(office)
                self.available_offices.pop(officeindex)
            person.office_name = office.name
            person.is_allocated = True
        else:
            cprint(f"{first_name.lower()} has not been allocated an office yet", color="yellow")

        if person_type.upper() == "FELLOW" and wants_accommodation:
            #person = Fellow(first_name, last_name, wants_accommodation)
            #cprint(f"{first_name, last_name} has been added successfully", color="blue")
            #self.added_people[person.name] = person
            #is_added = True
            #self.names_of_all_added_people.append(person.name)
            if len(self.available_livingspaces) != 0:
                livingspace = random.choice(self.available_livingspaces)
                cprint(f"{first_name.lower()} has been allocated livingspace {livingspace.name}", color="green")
                livingspace.members.append(person)
                if livingspace.is_full():
                    livingspaceindex = self.available_livingspaces.index(livingspace)
                    self.available_livingspaces.pop(livingspaceindex)
                person.livingspace_name = livingspace.name
                person.is_allocated = True 
            #if not wants_accommodation
            #else: 
            # False
            else:
                cprint(f"{first_name.lower()} has not been allocated an livingspace yet", color="yellow")

                #if wants_accommodation:
                #   if len(self.available_livingspaces) != 0:
                #       livingspace = random.choice(self.available_livingspaces)
                #    cprint(f"{first_name.lower()} has been allocated livingspace {livingspace.name}", color="blue")
                #    livingspace.members.append(person)
                    
                #    person.livingspace_name = livingspace.name
                #    person.is_allocated = True if person.office_name and person.livingspace_name else False
                #else:
                #    cprint(f"{person.name} has not been allocated a living space as yet! create some rooms to add them", color="yellow")
        return is_added
    
    
    
    def print_room(self, room_name):
        """prints a room specified by name:
            :returns True if it has printed the room,or
            False otherwise
        """
        room_name = room_name.upper()
        if room_name not in self.names_of_all_created_rooms:
            cprint(
                f"a room with name {room_name} doesn't exist in the Dojo", color="red")
            return False
        print(self.all_created_rooms[room_name])
        return True
    
    def print_allocations(self, filename=None):
        """ prints all rooms clearly showing the room in which a particular
        person was added to. If filename is specified, the allocations are
        saved in that file; else they are printed to the standard output
        """
        if len(self.all_created_rooms) == 0:
            cprint("no rooms found", color="red")
            return False

        if filename is None:
            for room in self.all_created_rooms.values():
                # if not room.is_empty():
                line_1_string = 'ROOM ' + room.name.upper() 
                print(line_1_string)
                print('------------------------------------')
                room_members = []
                
                for member in room.members:
                    room_members.append(member.name.upper())
                print(', '.join(room_members))
                
                print('\n')
        else:
            with open(filename, mode="w", encoding="UTF-8") as fh:
                for room in self.all_created_rooms.values():
                    # if not room.is_empty():
                    fh.write("\n".join([str(room)]))
        return True

    def print_unallocated(self, filename=None):
        """ prints unallocated people showing the type of rooms that they need to get.
        if filename is specified, the information will be saved there else it is
        printed to standard output
        """
        if len(self.all_created_rooms) == 0:
            cprint("no rooms found", color="red")
            return False

        if len(self.added_people) == 0:
            cprint("no people in the dojo yet!", color="red")
            return False

        unallocated = []
        for person in self.added_people.values():
            if not person.is_allocated:
                unallocated.append(person)

        if not unallocated:
            cprint("all people in the dojo have been allocated rooms", color="blue")
            return False

        unallocated_offices = []
        unallocated_livingspaces = []
        for person in unallocated:
            if person.type_ == "Staff" or (person.type_ == "Fellow" and person.office_name is None):
                unallocated_offices.append(person.name)
            if person.type_ == "Fellow" and person.wants_accommodation and person.livingspace_name is None:
                unallocated_livingspaces.append(person.name)
        if filename is not None:
            with open(filename, mode="w", encoding="UTF-8") as fh:
                if unallocated_livingspaces:
                    fh.write("Those without a living space:\n{}\n\n".format(
                        ", ".join(unallocated_livingspaces)))
                if unallocated_offices:
                    fh.write("Those without an office:\n{}\n".format(
                        ", ".join(unallocated_offices)))

        else:
            if unallocated_livingspaces:
                print(
                    f"Those without a living space:- {', '.join(unallocated_livingspaces)}")
            if unallocated_offices:
                print(
                    f"Those without an office are:- {', '.join(unallocated_offices)}")
        return True

    def reallocate_person(self, name, new_room_name):
        """ Reallocates a person to a room. useful when a person is added
            without allocating them a room or for shifting people within rooms. """
        name = name.upper()
        if name.upper() not in self.names_of_all_added_people:
            cprint(
                f"person with name '{name}' has not been added to the Dojo", color="red")
            return False

        room_name = new_room_name.upper()
        if room_name not in self.names_of_all_created_rooms:
            cprint(
                f"room with name '{new_room_name}' has not yet been created", color="red")
            return False

        is_reallocated = False
        person = self.added_people[name]
        room = self.all_created_rooms[room_name]
        if not room.is_full():
            if room.type_ == "Office":
                if person.office_name != room.name:
                    is_reallocated = True
                    cprint(
                        f"{person.name} has been reallocated from {person.office_name} to {room.name}", color="blue")
                    if person.office_name is not None:
                        self.all_created_rooms[person.office_name].members.remove(
                            person)
                    person.office_name = room.name
                    room.members.append(person)
                else:
                    cprint(
                        f"{person.name} is already in Room '{room.name}'", color='yellow')
                if person.type_ == "Staff" or (person.type_ == "Fellow" and not person.wants_accommodation):
                    person.is_allocated = True

            if room.type_ == "LivingSpace":
                if person.type_ == "Staff":
                    cprint(
                        "staff members cannot be accommodated at the Dojo", color="red")
                    return False

                if person.wants_accommodation:
                    if person.livingspace_name != room.name:
                        is_reallocated = True
                        cprint("{} has been reallocated from {} to {}".format(person.name, person.livingspace_name,
                                                                                room.name), color="blue")
                        if person.livingspace_name is not None:
                            self.all_created_rooms[person.livingspace_name].members.remove(
                                person)
                        person.livingspace_name = room.name
                        room.members.append(person)
                    else:
                        cprint(
                            f"{person.name} is already in Room '{room.name}'", color='yellow')
                        return False

                    if person.office_name:
                        person.is_allocated = True
                else:
                    cprint(f"{person.name} never wanted to be accommodated in the Dojo "
                                    "and hence cannot be accommodated", color="red")
                    return False
        else:
            cprint(
                f"{name} cannot be reallocated to Room {room_name} since {room_name} is full", color="red")
        return is_reallocated

    def load_people(self, filename):
        """Loads people from a text file and adds them to the Dojo"""
        has_loaded = False
        fh = None
        try:
            fh = open(filename, mode="r", encoding="UTF-8")
            for line in fh:
                person_args = line.lower().split()
                if len(person_args) > 3:
                    self.add_person(
                        person_args[0], person_args[1], person_args[2], person_args[3])
                else:
                    self.add_person(
                        person_args[0], person_args[1], person_args[2], "n")
        except OSError as err:
            cprint(f"failed to load {filename}: {err}", color="red")
        else:
            has_loaded = True
            cprint("All people have been loaded successfully from '{}'".format(
                filename), color="green")
        finally:
            if fh is not None:
                fh.close()
        return has_loaded
    
    
    
    def connect_to_db(self, db_name):
        """Helper function to connect to database"""
        self.db = create_engine("sqlite:///" + db_name)
        session = sessionmaker()
        session.configure(blind=self.db)
        Base.metadata.create_all(self.db)
        
        storage_session = session()
        return storage_session
        
    def save_state(self, args):
        """Takes up an optional argument --db that 
        specifies the database to store the data
        in the rooms and people dictionary. 
        Creates database and save data"""
        
        
        self.db_name = "dojo.db"
        if args["--db"]:
            self.db_name = args["--db"]
            
            
        # check if the database exists, if it does, delete the existing.
        
        if os.path.exists(self.db_name):   
            os.remove(self.db_name)
            
        try:
            save_session = self.connect_to_db(self.db_name)
            self.save_people(save_session)
            self.save_rooms(save_session)
            self.save_allocations(save_session)    
            
            message = "Data has been stored in the {} database".format(
                self.db_name)

        except Exception:
            message = "Error saving data to {}".format(self.db_name)

        save_session.commit()
        save_session.close()

        return message



    def save_people(self, storage_session):
        """
        Loads data from the people_data dict into the database
        """
        try:
            for key, values in People.items():
                #person_id = key
                first_name = values["first_name"]
                last_name = values["last_name"]
                person_type = values["person_type"]
                wants_accommodation = values["accommodation"]
            

                people = People(first_name=first_name, last_name=last_name,
                                person_type=person_type, wants_accommodation=wants_accommodation,
                                )
                storage_session.add(people)
                
            return people
        except Exception:
            return "Failed"

    def save_rooms(self, storage_session):
        """
        Loads data from the rooms dict into the database
        """
        try:
            for key, values in Rooms.items():
                room_name = key
                room_type = values["room_type"]
                room_data = Rooms(room_name=room_name, room_type=room_type)

                storage_session.add(room_data)

            return room_data
        except Exception:
            return "Failed"

    #def save_allocations(self, storage_session):
    #    """
    #   Loads data of room allocations into allocations table
    #    """
    #    try:
    #        for key, values in Rooms.items():
    #            room_name = key
    #            for identifier in values["occupants"]:
    #                occupant_id = identifier
    #
    #                allocation_data = Allocations(room_name=room_name,
    #                                              occupant_id=occupant_id)
    #                storage_session.add(allocation_data)

    #       return allocation_data
    #    except Exception:
    #       return "Failed"