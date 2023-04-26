#!/usr/bin/python3
"""
This module accommodate the function is_same_class
"""


def is_same_class(obj, a_class):
    """remit true if obj is the exact class a_class, else wrong"""
    return (type(obj) == a_class)
