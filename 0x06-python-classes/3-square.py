"""Create a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new a square
        Args:
            size (int) - represent a new square defined
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """returns the current area"""
            return (self.__size * self.__size)
  