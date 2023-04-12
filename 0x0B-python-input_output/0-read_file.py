#!/usr/bin/python3
"""0-read_file.
Reads from file and prints.
"""


def read_file(filename=""):
    """Reads from filename and prints
    the contents to stdout.
    Args:
        - filename: title of the file
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
