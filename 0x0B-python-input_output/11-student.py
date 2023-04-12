#!/usr/bin/python3
"""Component 11-student.
Generates a Student class.
"""


class Student:
    """Class that establish a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    Public method reload_from_json().
    """

    def __init__(self, first_name, last_name, age):
        """Establishes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Resolve a dictionary representation
        of a Student instance.
        Args:
            - attrs: list of imputes
        Remits: the dict representation of the instance.
        """

        my_dict = dict()
        if attrs and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Restore all imputes of the Student instance.
        Args:
            - json: dictionnary of attributes
        """

        for x in json:
            self.__dict__.update({x: json[x]})
