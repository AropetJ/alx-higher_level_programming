#!/usr/bin/python3
# base.py
import json
import csv


class Base():
    """ The base class for all my classes """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + "json"
        json_string = "[]"

        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
        
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return ([])
        else:
            return (json.loads(json_string))
    
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1,1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)

        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
        except FileNotFoundError:
            return ([])

        dict_list = cls.from_json_string(json_data)
        return ([cls.create(**dictionary) for dictionary in dict_list])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[3]), int(row[2]), int(row[0]))
                    instance_list.append(instance)
        except FileNotFoundError:
            return []
        
        return instance_list
