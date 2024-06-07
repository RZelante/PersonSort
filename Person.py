from pickle import TRUE


class Person:
    """
    Person class definition
    """

    def __init__(self, firstName, lastName):
        """
        constructs a Person object
        """
        self.firstName = firstName
        self.lastName  = lastName

    def __str__(self):
        """
        returns the string representation of an Person object
        the string should include the last name followed by a comma and the first name
        """
        s = self.lastName + "," + self.firstName
        return s

    def __eq__(self, other):
        """
        compares two Person objects
        returns true if the second Person object is equal to the first Person object
        comparison based on first and last names
        """
        if (self.lastName==other.lastName and self.firstName==other.firstName):
            return True
        else:
            return False

    def __lt__(self, other):
        """
        compares two Person objects
        returns true if the second Person object is < the first Person object
        comparison based on alphabetical order, last names compared first, then first names
        """
        # check for the same names
        if (self == other):
            return False
        
        # check if this lastName is less than the other lastName
        if (self.lastName < other.lastName):
            return True
        
        # check if the other lastName is less than this lastName
        if (other.lastName < self.lastName):
            return False

        
        # compare firstName's
        return (self.firstName < other.firstName)


