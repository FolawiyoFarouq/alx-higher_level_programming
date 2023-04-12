#!/usr/bin/python3
"""Component 8-class_to_json.
Remits the dictionary explanation with
plain data construction (list, dictionary,
string, integer and boolean)
for JSON sequential of an object.
"""


def class_to_json(obj):
    """Generates a dict explanation of obj.
    Args:
        - obj: object to serialize
    Remits: dictionary description of obj
    """

    return obj.__dict__

