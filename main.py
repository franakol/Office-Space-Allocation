import cmd
import os

from docopt import DocoptExit, docopt
from termcolor import cprint
from pyfiglet import Figlet, Default_Font

from app.control import Dojo


def intro():
    print(__doc__)


def docopt_cmd(func):
    """
    this is a decorator that simplifies the try/except block 
    and returns the results of parsing docopt using an action.
    """

    def fn(self, args):
        try:
            opt = docopt(fn.__doc__, args)

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

    fn.__doc__ = func.__name__
    fn.__doc__ = func. __doc__
    fn.__dict__.update(func.__dict__)
    return fn


class App(cmd.cmd):
    os.system("cls")
    prompt = "DojoRoomAllocator >>> "

    font = Figlet(Default_Font)
    cprint("{}{}".format(font.renderText(
        "Dojo\nRoom Allocator"), __doc__,), color="green")

    def __init__(self):
        super(App, self).__init__()
        self.dojo = Dojo()
