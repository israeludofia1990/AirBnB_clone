#!/usr/bin/python3
"""Entry point of the command interpreter"""


import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "
    # creating this to store valid classes
    __base_classes = ["BaseModel", "User", "State",
                      "City", "Place", "Amenity", "Review"]

    def do_quit(self, line):
        """Command to exit the interpreter"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""

        # split the command line argument
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in self.__base_classes:
                print("** class doesn't exist **")
            else:
                # getting the class from globals
                class_object = globals()[class_name]
                created_instance = class_object()
                print(created_instance.id)
                storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__base_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_id = args[1]
        # getting the __objects dict from storage
        storage_objects_dict = storage.all()
        for key in storage_objects_dict.keys():
            split_key = key.split('.')  # to check both parts of the key
            if len(split_key) == 2:
                model_name = split_key[0]
                model_id = split_key[1]

                if (model_name == class_name) and (model_id == class_id):
                    print(storage_objects_dict[key])
                    return
        print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__base_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_id = args[1]
        storage_objects_dict = storage.all()
        for key in storage_objects_dict.keys():
            split_key = key.split('.')
            if len(split_key) == 2:
                model_name = split_key[0]
                model_id = split_key[1]

                if (model_name == class_name) and (model_id == class_id):
                    del(storage_objects_dict[key])
                    storage.save()
                    return
        print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances"""
        args = line.split()
        if len(args) != 0:
            class_name = args[0]
            if class_name not in self.__base_classes:
                print("** class doesn't exist **")
                return

        all_list = []
        for val in storage.all().values():
            all_list.append(val.__str__())
        print(all_list)

    def do_update(self, line):
        """Updates an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__base_classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        seen = False
        class_id = args[1]
        storage_objects_dict = storage.all()
        for key in storage_objects_dict.keys():
            split_key = key.split('.')
            if len(split_key) == 2:
                model_name = split_key[0]
                model_id = split_key[1]

                if (model_name == class_name) and (model_id == class_id):
                    seen = True
                    break
        if not seen:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        elif len(args) == 3:
            print("** value missing **")
            return
        """
        obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v

        storage.save()
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
