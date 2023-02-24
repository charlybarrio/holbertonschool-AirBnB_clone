#!/usr/bin/python3
'''Store first objects'''
import json


class FileStorage:
    '''Serializes and deserializes file'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''return dictionarty objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <classname>.id'''
        cls_name = type(obj).__name__
        key = cls_name + "." + obj.id


    def save(self):
        '''to the JSON file'''
        srlz_file = json.dumps(FileStorage.objects) 

    def reload(self):
        '''to python objs'''
        if not FileStorage.__file_path:
            return
        else:
            with open(FileStorage.__file_path, 'w') as fp:
                json.load(__object, fp)

