#!/usr/bin/python3
'''Define json file-writing fuction.'''
import json


def save_to_file(my_obj, filename):
    '''Write object to text file using json representation.'''
    with open(filename, 'w') as f:
        jdon.dump(my_obj, f)
