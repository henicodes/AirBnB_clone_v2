#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
<<<<<<< HEAD


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
=======
import shlex


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
>>>>>>> 71d07a9c70ef4a945fe64b700790f904ea71b58c
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return self.__objects
        else:
            dic_result = {}
            for key, val in self.__objects.items():
                name = key.split('.')
                if name[0] == cls.__name__:
                    dic_result.update({key: val})
            return dic_result

    def new(self, obj):
        """Adds new object to storage dictionary"""
=======
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
>>>>>>> 71d07a9c70ef4a945fe64b700790f904ea71b58c
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
<<<<<<< HEAD
        """Saves storage dictionary to file"""
=======
        """serialize the file path to JSON file path
        """
>>>>>>> 71d07a9c70ef4a945fe64b700790f904ea71b58c
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
<<<<<<< HEAD
        """Loads storage dictionary from file"""
=======
        """serialize the file path to JSON file path
        """
>>>>>>> 71d07a9c70ef4a945fe64b700790f904ea71b58c
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        """ delete obj from __objects """
        if obj:
            for key in self.__objects:
                idn = key.split('.')
                if obj.id == idn[1]:
                    del self.__objects[key]
                    break
            self.save()

    def close(self):
        """ Calls reload() for deserializing the JSON file to objts"""
        self.reload()
=======
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()
>>>>>>> 71d07a9c70ef4a945fe64b700790f904ea71b58c
