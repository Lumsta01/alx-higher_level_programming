#!/usr/bin/python3
'''Define file-appending function.'''


def append_write(filename="", text=""):
    '''append string to of UTF-8 text file.

    Args:
        filename(str): Name of the file to append to.
        text(str): string to append to file.
    Returns:
        Number of chars appended.
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        num_char_app = f.write(text)
        return num_char_app
