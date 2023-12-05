#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import shlex  # for splitting strings into token, esp in parsing cmd-line input
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    my command interpreter
    """
    prompt = "(hbnb) "
    list_objClass = [
            "BaseModel"
            ]

    def do_quit(self, arg):
        """ Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program using CTRL+D"""
        print(disconnected)
        return True

    def emptyline(self):
        """do not execute anything"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id.
        Ex: $ create BaseModel
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.list_objClass:
            print("** class doesn't exist **")
        else:
            new_instance = globals()[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
         Prints the string representation of an instance
         based on the class name and id. Ex: $ show
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.list_objClass:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            """
            We have to check if the 'id' exists, to achieve that we need to
            create id_obj with the form Classname.id that is the key that
            we will use to ask if it is in Storage and
            can retrieve the value for that key, if the id_obj is not in
            storage then print 'no instance found'
            """
            id_obj = "{}.{}".format(args[0], args[1])
            if id_obj in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
