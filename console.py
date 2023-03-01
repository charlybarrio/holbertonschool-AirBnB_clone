#!/usr/bin/python3
'''entry point of the command interpreter'''
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity

classes = ["BaseModel", "User", "Place", "State", "Review", "City", "Amenity"]


class HBNBCommand(cmd.Cmd):
    ''' class for cmd'''
    prompt = '(hbnb)'

    def do_quit(self, args):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, args):
        '''Signal to exit safely to the program'''
        print("")
        return True

    def emptyline(self):
        '''Do nothing'''
        pass

    def do_create(self, args):
        """Create a new instance(saves it and print id)"""
        if not args:
            print("** class name missing **")
            return

        token = args.split()
        if token[0] not in classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(args)()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        """Prints the string representation of an instance"""
        token = args.split()

        if not args:
            print("** class name missing **")
        elif token[0] not in classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(token[0], token[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance"""
        token = args.split()
        if not args:
            print("** class name missing **")
        elif token[0] not in classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(token[0], token[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """ints all string representation of all instances"""
        token = args.split()
        objs = []

        if not args:
            objs = [str(obj) for obj in storage.all().values()]
        else:
            if token[0] in classes:
                objs = [str(obj) for obj in storage.all().values()
                        if obj.__class__.__name__ == token[0]]
            else:
                print("** class doesn't exist **")
                return
        print(objs)

    def do_update(self, args):
        """Updates an instance"""
        token = args.split()
        objs = storage.all()
        if not args:
            print("** class name missing **")
            return
        if token[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(token) < 2:
            print("** instance id missing **")
            return
        key = '{}.{}'.format(token[0], token[1])
        if key not in objs:
            print("** no instance found **")
            return
        if len(token) < 3:
            print("** attribute name missing **")
            return
        if len(token) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        name = token[2]
        val = token[3]
        if name not in obj.__dict__:
            print("** attribute doesn't exist **")
            return
        else:
            setattr(obj, name, val)
            obj.save()
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
