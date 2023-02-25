#!/usr/bin/python3
'''entry point of the command interpreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' class for cmd'''
    prompt = '(hbnb)'

    def quit(self, args):
        '''Quit command to exit the program'''
        return True

    def EOF(self):
        '''Signal to exit the program'''
        print(" ")
        return True

    def empty_line(self):
        '''Do nothing'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
