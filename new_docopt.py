#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    my_program create_room <host> <port> [--timeout=<seconds>]
    my_program add_person <first_name> <second_name> <FELLOW|STAFF> [<wants_accommodation>]
    my_program print_room <room_name>
    my_program load_people <filename>
    my_program print_allocations [<-o=filename>]
    my_program print_unallocated [<-o=filename>]
    my_program reallocate_person <first_name> <second_name> <new_room_name>
    my_program (-i | --interactive)
    my_program (-h | --help | --version)
Options:
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit

from app.control import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class App (cmd.Cmd):
    intro = 'Dojo Room allocation' \
        + ' (type help for a list of commands.)'
    prompt = '(Dojo Room Allocation) '
    file = None
    dojo = Dojo()

    # def __init(self):
    #    self.dojo = Dojo()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_names> [--timeout=<seconds>]"""
        room_type = arg['<room_type>']
        room_names = arg['<room_names>'].split(',')
        #print(room_type, room_names)
        # print(arg)
        self.dojo.create_room(room_type, room_names)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <second_name> <FELLOW_or_STAFF> [<wants_accommodation>]"""
        first_name = arg["<first_name>"]
        second_name = arg["<second_name>"]
        person_type = arg["<FELLOW_or_STAFF>"]
        wants_accommodation = arg["<wants_accommodation>"]
        self.dojo.add_person(first_name, second_name,
                            person_type, wants_accommodation)
        print('\n')

    @docopt_cmd
    def do_print_room(self, args):
        """ Usage: print_room <room_name>"""
        room_name = args["<room_name>"]
        self.dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [<-o=filename>]"""
        filename = args["<-o=filename>"]
        if filename:
            self.dojo.print_allocations(filename)
        else:
            self.dojo.print_allocations()

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [<-o=filename>]"""
        filename = args["<-o=filename>"]
        if filename:
            self.dojo.print_unallocated(filename)
        else:
            self.dojo.print_unallocated()

    @docopt_cmd
    def do_load_people(self, args):
        """ Usage: load_people <filename>"""
        self.dojo.load_people(args["<filename>"])

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <first_name> <second_name> <new_room_name>"""
        first_name = args["<first_name>"]
        second_name = args["<second_name>"]
        new_room_name = args["<new_room_name>"]
        name = "{} {}".format(first_name, second_name)

        self.dojo.reallocate_person(name, new_room_name)

    # @docopt_cmd
    # def do_clear(self, _):
    #   """usage: clear"""
    #   """clear clears the screen"""
    # os.system("cls")

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

App().cmdloop()

print(opt)
