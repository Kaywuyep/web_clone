#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    my command interpreter
    """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
