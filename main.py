
import os
import cmd
from docopt import docopt, DocoptExit
from app.dojo import Dojo

dojo = Dojo('DOJO1', 'The Dojo')

def get_docopt_args(func):
   """
   this is the decorator that will pass the results of the docscript command to the function.
   """

   def func_wrapper(self, args):
       try:
           opt = docopt(func_wrapper.__doc__, arg)
        except DocoptExit as e:
            return 
            except SystemExit:
                return

            return func(opt)
        func_wrapper.__name__ = func.__name__ 
        func_wrapper.__doc__ = func.__doc__ 
        func_wrapper.__dict__.update(func.__dict__)
        return func_wrapper

        class SpaceAllocation(cmd.cmd):
            """entry point for the application
            """
            os.system('cls')
            print("\nWelcome to the Dojo Space allocation app")
            print('\nLocation Name: ' + dojo.name + '\n')

            prompt = 'SpaceAllocation: ' # this prompt replaces the default cmd prompt message

            @get_docopt_args
            def do_create_room(params):
                """ to create_room <room_type> <room_name>..."""
                return dojo.create_room(params["<room_type>"], params["<room_name>"])

            @get_docopt_args
            def do_add_person(params):
                """ use: add_person <person_name> <person_type> [<wants_accommodation>]"""
                wants_accommodation = params["<wants_accommodation>"]
                if wants_accommodation == 'Y':
                    wants_accommodation = True
                    else:
                        wants_accommodation = False
                        return dojo.add_person(params["<person_name>"], params["<person_type>"], wants_accommodation)