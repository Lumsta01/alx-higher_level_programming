#!/usr/bin/python3
'''Define string to JSON function.'''
import json


def to_json_string(my_obj):
    '''Return JSON representation of string object.'''
    return json.dumps(my_obj)
