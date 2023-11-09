#!/usr/bin/python3
"""HBNBCommand interpreter class definition."""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter.
    Attributes:
        prompt: custom command prompt: (hbnb)
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the console."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the console."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
