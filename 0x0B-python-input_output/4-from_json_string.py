#!/usr/bin/python3
'''Define JSON-to-object function.'''
import json


def from_json_string(my_str):
    '''Return python object representation of json string.'''
    return json.loads(my_str)
