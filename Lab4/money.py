# Lab 4
# Dami Ibrahim
# The purpose of this lab is to demonstrate ADTs by implementing link-based lists and derivative ADTs
from currency import Currency

class Money(Currency):
    # This function contains the string attributes for the currency note and currency coin
    def _init_(self):
        __dollar = 0
        __coin = 0 
        __name = ''
    # Constructor
    # Pre: self - Instance of the class, dollar, and cent
    # Post:
    def __init__(self, dollar, coin, name):
        self.dollar = dollar
        self.coin = coin
        self.name = name
    # Setters
    def setDollar(self, dollar):
        self.dollar = dollar

    def setCoin(self, coin):
        self.coin = coin

    def setName(self, name):
        self.name = name
    # Getters
    def getDollar(self):
        return self.dollar

    def getCoin(self):
        return self.coin

    def getName(self):
        return self.name

    def _del_(self) :
        print("Destructor called!")
    # Add currency
    # Pre: node- used as another value to operate with the original value
    # Post: Returns the sum of the values
    def addCurrency(self, node):
        global dollar
        coin = self.coin + node.coin
        if coin > 99 :
            dollarPart = coin // 100
            coin = coin % 100
            dollar = self.dollar + node.dollar + dollarPart
        return dollar, coin

    # Subtraction same currency
    # Pre: node- used as another value to operate with the original value
    # Post: Returns the difference of the values
    def subtractCurrency(self, node):
        coin = 0
        dollar = 0
        if self.coin >= node.coin:
            coin = self.coin - node.coin
        else:
            coin = self.coin - node.coin + 100
            dollar = self.dollar - 1
            dollar += self.dollar - node.dollar
        return dollar, coin

    # Checking equality/inequality
    # Pre: node- used as another value to operate with the original value
    # Post: Returns True if the values are the same and False if they are not
    def equalCurrency(self, node):
        if self.name == node.name:
            if self.dollar == node.dollar:
                if self.coin == node.coin:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    # comapring currency whether
    # Pre: node- used as another value to operate with the original value
    # Post: Returns True if the original value is greater than the other value or if they are equal
    def greaterCurrency(self, node):
        if self.dollar > node.dollar:
            return True
        elif self.dollar == node.dollar:
            if self.coin > node.coin:
                return True
        else:
            return False

    # Prints currency
    def printCurrency(self) :
        print('The amount is: ', self.dollar, '.', self.coin, ' ', self._name)
