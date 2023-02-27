#!/usr/bin/python3
""" console """


import cmd 
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    clas = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print('')
        exit()
    
    def emptyline(self):
        pass

    def do_create(self, arg):
        """create command to exit the program"""
        if not arg:
            print("** class name missing **")
        aux = None
        if arg:
            separate_arg = arg.split()
            if len(separate_arg) == 1:
                if arg in self.clas.keys():
                    aux = self.clas[arg]()
                    aux.save()
                    print(aux.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """show command to exit the program"""
        if not arg:
            print("** class name missing **")
            return
        elif arg.split()[0] not in self.clas:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            aux = arg.split()[0] + '.' + arg.split()[1]
            if aux in storage.all():
                value = storage.all()
                print(value[aux])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """destroy command to exit the program"""
        if not arg:
            print("** class name missing **")
            return
        separate_arg = arg.split()
        try:
            aux = eval(separate_arg[0])
        except Exception:
            print("** class doesn't exist **")
        if len(arg) == 1:
            print("** instance id missing **")
        elif len(arg.split()) > 1:
            aux = arg.split()[0] + '.' + arg.split()[1]
            if aux in storage.all():
                storage.all().pop(aux)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        if not arg:
            print([str(aux) for aux in storage.all().values()])
        elif arg not in self.clas:
            print("** class doesn't exist **")
        else:
            print([str(aux) for key, aux in storage.all().items() if arg in key])

    def do_update(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg.split()[0] not in self.clas:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            aux = arg.split()[0] + '.' + arg.split()[1]
            if aux in storage.all():
                if len(arg) < 2:
                    if len(arg) == 3:
                        print("** value missing **")
                    else:
                        setattr(storage.all()[aux], arg[2], arg[3][1:-1])
                        storage.all()[aux].save()
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()