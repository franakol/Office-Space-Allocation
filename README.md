# Office-Space-Allocation

This system is a utility that shows how rooms are allocated at Andela's office facility in Kenya called the 'DOJO'

## Justification

When a new Staff joins Andela, they are assigned an office space only. When a new Fellow joins, they are assigned
an office space and a living space that is optional if they choose to to take it. therefore this mimics a working
model of how office and living space rooms are allocated.

### Instructions to use

To get started, you must have [python 3](https://www.python.org/) and [git](https://git-scm.com/) installed. clone this repo by running:

$ `git clone https://github.com/franakol/Office-Space-Allocation.git`

* install a virtual environment and configure it for the project.
```
$ pip install virtualenv
$ mkdir venv
$ virtualenv -p <path to your python executable> venv
$ cd venv/scripts/activate
```

* Inside your virtual environment, install dependencies
```
$ pip install -r requirements.txt
```
* Run the application
```
$ python new_docopt.py
```
#### Documentation

```
`create_room <room_type> <room_name>...()` creates a room or rooms of type room_type

`add_person <first_name> <second_name> <FELLOW|STAFF> [<wants_accommodation>]()` adds a person of either type fellow or staff to the dojo. wants_accommodation is an optional parameter.

`print_room <room_name>()` prints the details of a room specified by room_name

`load_people <filename>()` adds people to the dojo from filename if filename is not empty

print_allocations [<-o=filename>] prints all rooms in the dojo and all related information

`print_unallocated [<-o=filename>]()` prints unallocated people in the Dojo.

`reallocate_person <first_name> <second_name> <new_room_name>()` reallocates a person to new_room_name

`help()` displays the usage message

`clear()` Clears the application screen

`quit()` Exits the application



