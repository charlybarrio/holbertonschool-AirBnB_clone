#!/usr/bin/python3
'''entry point of the command interpreter'''
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
