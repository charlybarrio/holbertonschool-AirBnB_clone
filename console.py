#!/usr/bin/python3
'''entry point of the command interpreter'''
import cmd

classlist = ["BaseModel", "State", "City", "Amenity"]

class HBNBCommand(cmd.Cmd):
    ''' class for cmd'''
    prompt = '(hbnb)'

    def do_quit(self, args):
        '''Quit command to exit the program'''
        return True

    def do_eof(self, args):
        '''Signal to exit the program'''
        print(" ")
        return True

    def emptyline(self):
        '''Do nothing'''
        pass

    def do_create(self, args):
        """Create a new instance(saves it and print id)"""
        if not args:
            print("** class name missing **")
            return\
        
        token = args.split()
        if token[0] not in classlist:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(args)()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        token = args.split()

        if not args:
            print("** class name missing **")
        elif token[0] not in classlist:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(token[0], token[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

