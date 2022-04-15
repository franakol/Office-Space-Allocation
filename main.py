import sys
import os
import cmd
from docopt import docopt, DocoptExit
#from termcolor import cprint
#from pyfiglet import Figlet, Default_Font

from app.control import Dojo


# def intro():
#    print(__doc__)


def docopt_cmd(func):
    """
    this issudo apt-get install python3-pip a decorator that simplifies the try/except block 
    and returns the results of parsing docopt using an action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as err:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(err)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # No need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class App (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = 'Dojo Room Allocator:'
    file = None

    #font = Figlet(Default_Font)
    #cprint("{}{}".format(font.renderText(
    #    "Dojo\nRoom Allocator"), __doc__,), color="green")  #font = Figlet(Default_Font)
    #cprint("{}{}".format(font.renderText(
    #    "D

    #def __init__(self):
        #os.system("cls")
        #prompt = "DojoRoomAllocator >>> "
       # print('--here--')
        #super(App, self).__init__()
        #self.dojo = Dojo()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type>   <room_name>..."""
        #room_type = args["<room_type>"]
        #room_names = args["<room_name>"]
        #self.dojo.create_room(room_type, room_names)
        print('do_create-room')
        print(arg)
    
    @docopt_cmd
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        print(arg)
        exit()

opt = docopt(__doc__, sys.argv[1:])
App().cmdloop()
print(opt)