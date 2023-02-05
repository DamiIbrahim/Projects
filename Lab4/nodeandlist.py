# Lab 4
# Dami Ibrahim
# The purpose of this lab is to demonstrate ADTs by implementing link-based lists and derivative ADTs


class LinkNode:
    # Data and pointer attribute
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList(LinkNode):

    # Constructor/Creating a new list
    # Pre: start, end, data, and next are the instance attributes. Data and next are none types.
    # Post:
    def __init__(self, start, end, data=None, next=None):
        super().__init__()
        self.head = None
        count = 0
        self.start = start
        self.end = end
        self.data = data
        self.next = next


    # Setters for LinkedList
    def setCount(self, count = 0):
        self.count = count


    def setStart(self, start):
        self.start = start


    def setEnd(self, end):
        self.end = end


    # Getters for LinkedList
    def getCount(self,):
        return self.count


    def getStart(self):
        return self.start


    def getEnd(self):
        return self.end

    # Adding data to list
    # Pre: Data is the nodes in the list
    # Post: Returns the added nodes plus the original list
    def addData(self, data):
        list = []
        if data not in list :
            list.append(data)
            print('add {} into list'.format(str(data)))
            print(str(data))
        else :
            return False


    # Deleting data
    # Pre: deleteNode - The node that is deleted from the list
    # Post: Returns the original list but deletes a node.
    def deleteData(self, deleteNode):
        headData = self.head
        if headData == None:
            print ('List is empty!\n')
        if headData != None:
            if headData.data == deleteNode:
                self.head = headData.next
                headData = None
                return
        prev = None
        while headData != None:
            if headData.data == deleteNode:
                break
            prev = headData
            headData = headData.next
        if headData != None:
            return
        print('Remove {}'.format(headData))


    # Finding Data
    # Pre: self instance attribute
    # Post: Returns the node if it's found and node not found if it's not in the original list
    def findData(self):
        data = ''
        n = 0
        headData = self.head
        if headData == None:
            print('List is empty')
        else:
            while headData != None:
                if (headData.data) == (data):
                    n += 1
                headData = headData.next
            if n == 0:
                print('Node not found\n')
            else:
                print('Node found: {}\n'.format(int(headData.data)))

    # Counting Data
    # Pre: self instance attribute
    # Post: Returns the length of nodes in the list
    def countData(self):
        count = 0
        headData = self.head
        while headData != None:
            count += 1
            headData = headData.next
        print('Counted {} data nodes'.format(count))

    # Is list empty
    # Pre: self instance attribute
    # Post: Returns True if the list is empty and false if not
    def isEmpty(self):
        headData = self.head
        if headData == None:
            return True
        else:
            return False
    # Destroys List
    def destroyList(self) :
        print("List Destroyed!")
    # Prints all items in List
    # Pre: self instance attribute
    # Post: Prints all nodes in list
    def printList(self):
        printList = self.head
        while printList != None:
            print(printList.data)
            printList = printList.next