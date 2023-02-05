# Lab 3
# Name: Dami Ibrahim
# The purpose of this lab is to sort an array of data using the recursive insertion sort method
from currency import Currency

# Differences from Lab 2
# - I changed the currency note method to an initializer method
# - I changed the variables from 'name1' and 'name2' to 'note' and 'coin'


class Money(Currency):
    # This function contains the string attributes for the currency note and currency coin
    # Pre: self - Instance of the class, dollar, and cent
    # Post:
    def __init__(self):
        self.note = 'Dollar'
        self.coin = 'Cent'

