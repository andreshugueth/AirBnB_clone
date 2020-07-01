#!/usr/bin/python3
"""Console version"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    __classes = [
        "BaseModel",
        "AuxModel",
        "User",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State"
        ]

    def do_EOF(self, line):
        """
        EOF [command]:
        -------------
        End Of File, used to exit from the console.
        """
        return True

    def do_quit(self, line):
        """
        quit [command]:
        ---------------
        used to exit from the console.
        """
        return True

    def emptyline(self):
        """This is the override of the cmd default's
        emptyline method, which is called when an empty
        line is entered in response to the prompt.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(args[0] + '()')
            models.storage.save()
            print(new_inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif not args[0] in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                print(objects[key_find])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel
        """
        args = line.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)

        elif len(args) == 1:
            if args[0] in HBNBCommand.__classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == args[0]:
                        new_list.append(obj.__str__())
                print(new_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute (save
        the change into the JSON file).
        Ex: $ update BaseModel <valid id> attrib value
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")

        elif len(args) == 1:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

        elif len(args) == 2:
            key_find = args[0] + '.' + args[1]
            if key_find not in objects.keys():
                print("** no instance found **")
            else:
                print("** attribute name missing **")

        elif len(args) == 3:
            print("** value missing **")

        elif len(args) >= 4:
            obj = objects[args[0] + '.' + args[1]]

            if args[2] in obj.__dict__:
                val_type = type(obj.__dict__[args[2]])
                obj.__dict__[args[2]] = eval(args[3])
            else:
                obj.__dict__[args[2]] = eval(args[3])

        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
