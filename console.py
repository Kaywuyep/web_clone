#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import shlex  # for splitting strings into token, esp in parsing cmd-line input
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    my command interpreter
    """
    prompt = "(hbnb) "
    list_objClass = [
            "BaseModel",
            "User"
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
            retrieve the value for that key, if the id_obj is not in
            storage then print 'no instance found'
            """
            id_obj = "{}.{}".format(args[0], args[1])
            if id_obj in storage.all():
                print(storage.all()[id_obj])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = shlex.split(arg)
        if not args:
            print ("** class name missing **")
        elif args[0] not in HBNBCommand.list_objClass:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            """
            We have to check if the 'id' exists, to achieve that we need to
            create id_obj with the form Classname.id that is the key that
            we will use to ask if it is in Storage and
            delete the value for that key, if the id_obj is not in
            storage then print 'no instance found'
            """
            id_obj = "{}.{}".format(args[0], args[1])
            if id_obj in storage.all():
                del storage.all()[id_obj]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name.
        Ex: $ all BaseModel or $ all
        we used a loop and a list (my_list) to store the string representations
        of instances based on the class name. It checks if the
        first argument (args[0]) is present
        """
        my_list = []
        args = shlex.split(arg)
        if len(args) == 0:
            for key, value in storage.all().items():
                my_list.append(str(value))
            print(my_list)
        elif args[0] in HBNBCommand.list_objClass:
            for key, value in storage.all().items():
                if value.__class__.__name__ == args[0]:
                    my_list.append(str(value))
            print(my_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = shlex.split(arg)
        if not args or args[0] not in HBNBCommand.list_objClass:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            objects = storage.all()
            instance = "{}.{}".format(args[0], args[1])
            if instance in objects.keys():
                for value in objects.values():
                    try:
                        attr_type = type(getattr(value, args[2]))
                        args[3] = attr_type(args[3])
                    except AttributeError:
                        pass
                setattr(value, args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
