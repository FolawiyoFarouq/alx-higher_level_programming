#!/usr/bin/python3
"""Task 100-my_int. (Advanced)
Generates a class that take over from int.
"""


class MyInt(int):
    """Class taking over from int,
    But undo the action of != and ==.
    """

    def __eq__(self, other):
        """balance becomes imbalance."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Imbalance becomes balance."""

        return super().__eq__(other)
