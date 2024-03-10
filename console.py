#!/usr/bin/python3
""" Creating: HBNBCommand console class """
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class core """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit method to trigger the quit command

        Returns True
        """
        return True

    def do_EOF(self, arg):
        """
        End of file method to trigger the EOF command

        Returns True
        """
        if sys.stdin.isatty():
            print("")

        return True

    def do_help(self, arg):
        """
        Help method to trigger help command (manual)

        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF   help   quit\n")
        """
        cmd.Cmd.do_help(self, arg)

    def help_quit(self):
        """
        Pops a help manual for the quit command
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """
        Pops a help manual for the enf of file command
        """
        print("Type <EOF or (Ctrl+D)> to exit the program\n")

    def help_all(self):
        """
        Pops a help manual for all command
        """
        print("Usage: all className |> Example: all BaseModel")
        print("Prints all instances of a given class or all classes.\n")

    def help_create(self):
        """
        Pops a help manual for create command
        """
        print("Usage: create className |> Example: create BaseModel")
        print("Creates a new instance Model and saves it in a (.json).\n")

    def help_destroy(self):
        """
        Pops a help manual for destroy command
        """
        print("Usage: destroy className id")
        print("Example: destroy BaseModel 7da7da-fdfd1v-gdg787gd-hdh54")
        print("Deletes an instance from a .json.\n")

    def help_show(self):
        """
        Pops a help manual for show command
        """
        print("Usage: show className id")
        print("Example: show BaseModel 7da7da-fdfd1v-gdg787gd-hdh54")
        print("Displays a string representation of an instance.\n")

    def help_update(self):
        """
        Pops a help manual for update command
        """
        print("Usage: update className id attrName 'attrValue'")
        print("Example: update BaseModel 77da-fdv-7gd-h54 first_name 'Betty'")
        print("Updates an instance by adding or updating an attribute.\n")

    def emptyline(self):
        """ triggers empty line method """
        pass

    def core(self, ln):
        """
        trigger emptyline method if the ln is empty
        or
        prints an unknown syntax error if cmd doesn't exist

        Args:
            ln: command-line argument
        """
        if (ln == ''):
            return (self.emptyline())
        else:
            print("*** Unknown syntax: ", ln)

    def isValid(self, argValue, argCount):
        """
        validates command line
        parses the command arguments and displays errors
        based on the input(argValue)

        Args:
            argValue (list): Command-line arg string
            argCount (int): arguments count

        Returns:
            bool True if cmd-line is valid otherwise False
        """
        if (not argValue):
            print("** class name missing **")
            return (False)
        if (argValue[0] not in ["BaseModel", "User",
           "State", "City", "Amenity", "Place", "Review"]):
            print("** class doesn't exist **")
            return (False)
        if (len(argValue) < argCount):
            if (len(argValue) == 1):
                print("** instance id missing **")
            elif (len(argValue) == 2):
                print("** attribute name missing **")
            elif (len(argValue) == 3):
                print("** value missing **")
            return (False)
        return (True)

    def do_create(self, argValue):
        """
        Creates a new instance of BaseModel
        saves it and prints its id

        Args:
            argValue: command argument string
        """
        argV = argValue.split()
        if not self.isValid(argV, 1):
            return

        cls = {"BaseModel": BaseModel, "User": User, "State": State,
               "Amenity": Amenity, "Place": Place, "Review": Review}
        cls_name = argV[0]

        if cls_name not in cls:
            print("** class doesn't exist **")
            return

        newModel = cls[cls_name]()
        newModel.save()
        print(newModel.id)

    def do_show(self, argValue):
        """
        displays __str__ representation of an instance

        Args:
            argValue: command line argument value
        """
        argV = argValue.split()
        if not self.isValid(argV, 2):
            return

        objK = argV[0] + '.' + argV[1]
        objDict = storage.all()
        if (objK in objDict):
            print(objDict[objK])
        else:
            print("** no instance found **")

    def do_destroy(self, argValue):
        """
        Deletes an instance based on the cls name and its id

        Args:
            argValue (str): Command-line arg string
        """
        argV = argValue.split()
        if not self.isValid(argV, 2):
            return

        objK = argV[0] + '.' + argV[1]
        objDict = storage.all()
        if (objK in objDict):
            del objDict[objK]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, argValue):
        """
        Displays all __str__ representations of all instances

        Args:
            argValue (str): Command-line arg string
        """
        objDict = storage.all()
        if not argValue:
            print([str(obj) for obj in objDict.values()])
            return

        cls_name = argValue.split()[0]
        if cls_name not in ["BaseModel", "User", "State", "City",
           "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        print([str(obj) for objK, obj in objDict.items()
               if cls_name in objK])

    def do_update(self, argValue):
        """
        Updates an instance based on the cls names and its id
        by adding or updating attrs

        Args:
             argValue (str): Command-line arg string
        """
        argV = argValue.split()
        if not self.isValid(argV, 4):
            return

        objK = argV[0] + '.' + argV[1]
        objDict = storage.all()
        if (objK in objDict):
            obj = objDict[objK]
            setattr(obj, argV[2], argV[3])
            obj.save()
        else:
            print("** no instance found**")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
