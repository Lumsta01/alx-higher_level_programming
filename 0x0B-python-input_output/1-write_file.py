#!/usr/bin/python3
'''Define a file_writing function.'''


def write(filename="", text=""):
    '''Write a string to a UTF-8 text file.

    Args:
        filename(str): Name of file to write.
        text(str): Text to write to file.
    Returns:
        Number of characters added
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        num_chars_written = f.write(text)
        return num_chars_written
