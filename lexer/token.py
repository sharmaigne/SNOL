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
    
    # Checks if this token is equal to another token
    def __eq__(self, other):
        if isinstance(other, Token):
            return self.type == other.type and self.value == other.value
        return False

    # Returns the hash value of the token based on its type and value
    def __hash__(self):
        return hash((self.type, self.value))