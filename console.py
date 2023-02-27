#!/usr/bin/python3
""" console """


import cmd 

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print('')
        exit()
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()