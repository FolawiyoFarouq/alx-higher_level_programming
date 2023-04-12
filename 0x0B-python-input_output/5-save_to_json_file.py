#!/usr/bin/python3
"""Component 5-save_to_json_file.
Writes an Article to a text file,
using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj
    to title.
    Args:
        - my_obj: object to write
        - title: file to write into
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
