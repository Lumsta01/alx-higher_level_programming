#!/usr/bin/python3
'''Define text file insert function.'''

def append_after(filename="", search_string="", new_string=""):
    '''insert text sfter each line that cointains given string in a file.

    Args:
        filename(str): Name of file.
        search_string(str): String to search within file.
        new_string(str): String to insert.
    '''
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
