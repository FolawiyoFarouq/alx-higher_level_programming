#!/usr/bin/python3
"""Explains a function that joins assigns to objects."""


def add_attribute(obj, att, value):
    """Attach a new assignment to an object if possible.
    Args:
        obj (any): The object to add an assignment to.
        att (str): The title of the assignment to add to obj.
        value (any): The value of ass.
    Lifts:
        TypeError: If the assignment cannot be attached.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
