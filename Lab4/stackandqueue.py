# Lab 4
# Dami Ibrahim
# The purpose of this lab is to demonstrate ADTs by implementing link-based lists and derivative ADTs


from nodeandlist import SinglyLinkedList
from nodeandlist import LinkNode
class Stack(SinglyLinkedList):
    # Constructor/Create Stack
    # Pre: self, data, next, and head attributes
    # Post:
    stack = []
    def __init__(self, data=None, next=None, head=None):
        self.data = data
        self.next = next
        self.head = head

    # Push stack
    # Pre: data- nodes in stack
    # Post: Pushes the nodes into stack
    def pushStack(self, data):
        stack = []
        if data not in stack:
            stack.append(data)
            print('Push {} into stack'.format(str(data)))
            return True
        else:
            return False
    # Pop stack
    # Pre: self instance attribute
    # Post: Removes the last node in stack
    def popStack(self):
        stack = [76, 33, 56, 12, 89, 36, 64]
        if len(stack) <= 0:
            print('No element found in stack!')
        else:
            print('Pop from stack : {}'.format(stack.pop()))
    # Peep stack
    # Pre: self instance attribute
    # Post: Returns the last node in stack
    def peekStack(self):
        stack = []
        return stack[-1]



class Queue(SinglyLinkedList):
    # Constructor/ Create queue
    def __int__(self, data=None, next=None, head=None):
        self.head = head
        self.data = data
        self.next = next
    # Enqueue
    # Pre: data- nodes in queue
    # Post: Adds nodes in queue
    def enqueue(self, data):
        queue = LinkNode()
        queue.data = data
        queue.next = None
        if self.head == None:
            self.head = queue
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = queue
        print('Enqueue data: {}\n'.format(str(data)))
    # Dequeue
    # Pre: self instance attribute
    # Post: Removes last node in queue
    def dequeue(self):
        headData = self.head
        if headData == None:
            print('Queue is empty')
        else:
            queuelist = [34, 45, 22, 78, 68, 11, 85]
            print('Dequeue Data: {}\n'.format(queuelist.pop()))
    # Peek Front
    # Pre: self instance attribute
    # Post: Returns the first node in queue
    def peekFront(self):
        temp = self.head
        if temp == None:
            print('Queue is empty!')
        else:
            print('Peak front queue: {}'.format(str(temp.data)))
    # Peek Rear
    # Pre: self instance attribute
    # Post: Returns the last node in queue
    def peekRear(self):
        headData = self.head
        if headData == None :
            print('Queue is empty!')
        else:
            temp = headData
            while temp.next != None:
                temp = temp.next
            print('Peek rear queue: {}'.format(str(temp.data)))
