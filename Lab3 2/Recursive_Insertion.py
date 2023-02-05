# Lab 3
# Dami Ibrahim
# The purpose of this lab is to sort an array of data using the recursive insertion sort method
#import sys
#sys.stdout = open('output.txt', 'w')
from money import Money
import traceback

# This function takes in the parameters array and size and prints out the array after each recursive iteration by
# removing the last element of the array, placing it in a temporary array, and then placing it in the correct position.
# Pre: array - the numbers the user inputs
#      size - the length of the number the user inputs
# Post: returns the last number in the array and keeps iterating until it is sorted


def RecurInsSort(array, size=0):
    if size <= 1:
        return
    RecurInsSort(array, size - 1)
    print('Next iteration:')
    print(dollar, *cent)
    lastElement = array[size - 1]
    index = size - 2
    if index >= 0 and array[index].compareCurrency(lastElement) == 1:
        array[index + 1] = array[index]
        index = index - 1
    array[index + 1] = lastElement
    return lastElement

def main():
    while True:
        size = 0
        array_size = int(input("Enter a size of array: "))
        array = [None] * array_size
        if not 1 <= array_size <= 16:
            print('Invalid input of array')
        if 1 <= array_size <= 16:
            print(array)
            for element in range(array_size):
                while True:
                    try:
                        array_list = []
                        dollar, *cent = [int(element) for element in input("Enter value: ").split(".")]
                        print(dollar, 'Dollar', *cent, 'Cent')
                        array_list.append(dollar)
                        #print(array_list)
                        break
                    except:
                        print("Invalid input")
                print(array_list)
            print('Calling RecurInsSort')
            RecurInsSort(array)
            print('Sorted array:')


if __name__ == '__main__':
    main()
