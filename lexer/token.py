class Token:
    """A class to represent a token. A token has a type and a value.

    The type is a string that represents the type of the token, such as 'NUMBER' or 'ADD'.

    The value is the actual value of the token, such as 2 or 'ADD'."""

    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"

    def __repr__(self):
        return self.__str__()