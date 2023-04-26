#!/usr/bin/python3
"""
Accommodate the inherits_from function
"""


def inherits_from(obj, a_class):
    """remits accurate if obj is a subclass of a_class, else not decline"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
