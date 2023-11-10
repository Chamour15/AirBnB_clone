#!/usr/bin/python3
"""HBNBCommand interpreter class definition."""
import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter.
    Attributes:
        prompt: custom command prompt: (hbnb)
    """
    prompt = "(hbnb) "
    __clss = {"BaseModel", "State", "City", "Amenity", "Place", "Review"}

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Usage: $ create BaseModel"""
        cmd_line = [i.strip(",") for i in split(arg)]
        if len(cmd_line) < 1:
            print("** class name missing **")
        elif cmd_line[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
        else:
            print(eval(cmd_line[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Usage: $ show BaseModel 1234-1234-1234."""
        cmd_line = [i.strip(",") for i in split(arg)]
        inst_id = storage.all()
        if len(cmd_line) == 0:
            print("** class name missing **")
        elif cmd_line[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif f"{cmd_line[0]}.{cmd_line[1]}" not in inst_id:
            print("** no instance found **")
        else:
            print(inst_id[f"{cmd_line[0]}.{cmd_line[1]}"])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Usage: $ destroy BaseModel 1234-1234-1234"""
        cmd_line = [i.strip(",") for i in split(arg)]
        inst_id = storage.all()
        if len(cmd_line) == 0:
            print("** class name missing **")
        elif cmd_line[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif f"{cmd_line[0]}.{cmd_line[1]}" not in inst_id.keys():
            print("** no instance found **")
        else:
            del inst_id[f"{cmd_line[0]}.{cmd_line[1]}"]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name. Usage: $ all BaseModel or $ all"""
        cmdline = [i.strip(",") for i in split(arg)]
        if len(cmdline) > 0 and cmdline[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
        else:
            _object = []
            for obj in storage.all().values():
                if len(cmdline) == 0:
                    _object.append(obj.__str__())
                elif len(cmdline) > 0 and cmdline[0] == obj.__class__.__name__:
                    _object.append(obj.__str__())
            print(_object)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        cmd_line = [i.strip(",") for i in split(arg)]
        objs = storage.all()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return False
        if cmd_line[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
            return False
        if len(cmd_line) == 1:
            print("** instance id missing **")
            return False
        if f"{cmd_line[0]}.{cmd_line[1]}" not in objs.keys():
            print("** no instance found **")
            return False
        if len(cmd_line) == 2:
            print("** attribute name missing **")
            return False
        if len(cmd_line) == 3:
            try:
                type(eval(cmd_line[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(cmd_line) == 4:
            obj = objs[f"{cmd_line[0]}.{cmd_line[1]}"]
            if cmd_line[2] in obj.__class__.__dict__.keys():
                value = type(obj.__class__.__dict__[cmd_line[2]])
                obj.__dict__[cmd_line[2]] = value(cmd_line[3])
            else:
                obj.__dict__[cmd_line[2]] = cmd_line[3]
        elif type(eval(cmd_line[2])) == dict:
            obj = objs[f"{cmd_line[0]}.{cmd_line[1]}"]
            for k, val in eval(cmd_line[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(val)
                else:
                    obj.__dict__[k] = val
        storage.save()

    def default(self, line):
        """retrieve instances by class name."""
        cmd = {
            "all": self.do_all,
        }
        regular = re.search(r"\.", line)
        if regular is not None:
            cmdl = [line[:regular.span()[0]], line[regular.span()[1]:]]
            _regular = re.search(r"\((.*?)\)", cmdl[1])
            if _regular is not None:
                command = [cmdl[1][:_regular.span()[0]], _regular.group()[1:-1]]
                if command[0] in cmd.keys():
                    return cmd[command[0]](f"{cmdl[0]} {command[1]}")
        print(f"*** Unknown syntax: {line}")
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
