# Lab 4
# Dami Ibrahim
# The purpose of this lab is to demonstrate ADTs by implementing link-based lists and derivative ADTs

# Differences from Lab 2
# - I included the operations in the init method for dollar and cent
# - I changed the variables to dollar and cent to make it less confusing when calling functions
# - I removed the add, subtract, and compare methods because it was not needed in this lab
class Currency:
    # constructor
    def __init__(self, dollar=0, cent=0):
        self.dollar = dollar + cent // 100
        self.cent = cent % 100

    # The setter functions initializes the two integer attributes.
    # Pre: self - The instance of the class that is being accessed using the constructor
    #      dollar - Represents the 'Dollar' portion of the long form value
    #      cent - Represents the 'Cent' portion of the long form value
    # Post:

    def setDollar(self, dollar):
        self.dollar = dollar

    def setCent(self, cent):
        self.dollar = cent + cent // 100
        self.cent = cent % 100

    # The getter functions return the two integer attributes
    # Pre: self- instance of the class being and allows us to access the attributes in the constructor for whole and fraction
    # Post:
    def getDollar(self):
        return self.dollar

    def getCent(self):
        return self.cent

