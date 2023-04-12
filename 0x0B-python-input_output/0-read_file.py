#!/usr/bin/python3

'''Define text reading fuction.'''


def read_file(filename=""):
    '''Print the contents of UTF-8 text file to stdout.'''
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(contents, end='')
