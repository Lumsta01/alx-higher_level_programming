#!/usr/bin/python3
'''Defines a JSON file-reading function.'''
import json


def load_from_json_file(filename):
    '''Create Python object from JSON file.'''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

