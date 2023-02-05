# Lab 6
# Dami Ibrahim
# The purpose of this lab is to demonstrate the use of hash tables and qudratic probing to hash the money objects from prior labs


#declaring a hash table of size 29
initial_size=29

class hashTable:
    # initialize hash Table
    # Pre: self instance of class
    # Post: 
    def __init__(self):
        self.size = int(input("Enter the Size of the hash table : "))
        # initialize table with all elements 0
        self.table = list(0 for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0
   
    # method that checks if the hash table is full or not
    # Pre: self instance attribute
    # Post: Returns True if hash table is full and False if not
    
    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False
   
   
    # method that returns position for a given element
    # Pre: self instance attribute, element is integer
    # Post: Returns the modulo of element and size of hash table
  
    def hashFunction(self, element):
        
        return element % self.size
       
   
    # method to resolve collision by quadratic probing method
    # Pre: self instance attribute, element is integer, position is position in hash table.
    # Post: Returns the new calculated position
    def quadraticProbing(self, element, position):
        posFound = False
        
        limit = 50
        i = 1
        # start a loop to find the position
        while i <= limit:
            # calculate new position by quadratic probing
            newPosition = position + (i**2)
            newPosition = newPosition % self.size
            # if newPosition is empty then break out of loop and return new Position
            if self.table[newPosition] == 0:
                posFound = True
                break
            else:
                # as the position is not empty increase i
                i += 1
        return posFound, newPosition
 
       
    # method that inserts element inside the hash table
    # Pre: self instance attribute, element is integer
    # Post: Returns True if position found is empty and prints out the position and element, or returns that a collision occured if position is not empty
    def insert(self, element):
        # checking if the table is full
        if self.isFull():
            print("Hash Table Full")
            return False
           
        isStored = False
       
        position = self.hashFunction(element)
           
        # checking if the position is empty
        if self.table[position] == 0:
            # empty position found , store the element and print the message
            self.table[position] = element
            print("Element " + str(element) + " at position " + str(position))
            isStored = True
            self.elementCount += 1
       
        # collision occured hence we do linear probing
        else:
            print("Collision has occured for element " + str(element) + " at position " + str(position) + " finding new Position.")
            isStored, position = self.quadraticProbing(element, position)
            if isStored:
                self.table[position] = element
                self.elementCount += 1
 
        return isStored
       
 
    # method that searches for an element in the table
    # Pre: self instance attribute, element is integer
    # Post: returns position of element if found, else returns False
    
    def search(self, element):
        found = False
       
        position = self.hashFunction(element)
        self.comparisons += 1
        if(self.table[position] == element):
            return position
       
        # if element is not found at position returned hash function
        # then we search element using quadratic probing
        else:
            limit = 50
            i = 1
            newPosition = position
            # start a loop to find the position
            while i <= limit:
                # calculate new position by quadratic probing
                newPosition = position + (i**2)
                newPosition = newPosition % self.size
                self.comparisons += 1
               
                # if element at newPosition is equal to the required element
                if self.table[newPosition] == element:
                    found = True
                    break
                   
                elif self.table[newPosition] == 0:
                    found = False
                    break
                   
                else:
                    # as the position is not empty increase i
                    i += 1
            if found:
                return newPosition
            else:
                print("Invalid Data")
                n=input("Would you like to do another task, press 1 to continue, 0 to exit:")
                if n==1:
                    return 0
                if n==0:
                    import sys
                    sys.exit()

                return found  
              

 
    # method to remove an element from the table
    # Pre: self instance attribute, element is integer
    # Post: If element is in the right position returns that it is deleted, returns it is not present in hash table if not found at position.
    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(element) + " is Deleted")
            self.elementCount -= 1
        else:
            print("Element is not present in the Hash Table")
        return
       
   
    # method to display the hash table
    # Pre: self instance attribute
    # Post:
    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("The number of element is the Table are : " + str(self.elementCount))
        load_factor=int(self.elementCount)/29
        print("The load Factor is: ",load_factor)
       
           
# main function
table1 = hashTable()
 
# storing data elements in table
table1.insert(10)
table1.insert(32)
table1.insert(321)
table1.insert(18)
table1.insert(76)
table1.insert(33)
table1.insert(8)
table1.insert(70)
table1.insert(77)       # element that causes collision at position 0
 
# displaying the Table
table1.display()
print()
 
# printing position of elements
print("The position of element 31 is : " + str(table1.search(18)))
print("The position of element 28 is : " + str(table1.search(321)))
print("The position of element 90 is : " + str(table1.search(90)))

print("\nTotal number of comparisons done for searching = " + str(table1.comparisons))
print()
 


#el=input("input an element to search: ")
#print("The position of element 31 is : " + str(table1.search(el)))

