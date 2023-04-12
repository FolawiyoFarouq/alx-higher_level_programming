#!/usr/bin/python3
"""Components 100-append_after.
Puta line of text to a file,
after each line containing a particular string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends the new_string after
    the search_string in filename.
    Args:
        - filename: name of the file
        - search_string: string to attach after
        - new_string: new_string to attach
    """

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
