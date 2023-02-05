# Lab 4
# Dami Ibrahim
# The purpose of this lab is to demonstrate ADTs by implementing link-based lists and derivative ADTs


import nodeandlist
import stackandqueue

def main():
    print('Linked List testing.....\n\n')

    linkedList = nodeandlist.SinglyLinkedList(start=int(), end=int())
    print(linkedList.addData('50'))
    print(linkedList.addData('100'))
    print(linkedList.addData('66'))
    print(linkedList.addData('9'))
    print(linkedList.addData('50'))
    print(linkedList.addData('32'))
    print(linkedList.addData('12'))
    print(linkedList.printList())
    print('Delete 50 from list')
    print(linkedList.deleteData('50'))
    (linkedList.countData())
    print(linkedList.findData())

    print('Stack testing.....\n\n')
    stackList = stackandqueue.Stack(list())
    stackList.pushStack(76)
    stackList.pushStack(33)
    stackList.pushStack(56)
    stackList.pushStack(12)
    stackList.pushStack(89)
    stackList.pushStack(36)
    stackList.pushStack(64)
    print('List: 76, 33, 56, 12, 89, 36, 64')
    print('Pop stack once')
    print(stackList.popStack())

    print('Queue testing.....\n\n')
    queueList = stackandqueue.Queue(start=int(), end=int())
    queueList.enqueue(34)
    queueList.enqueue(45)
    queueList.enqueue(22)
    queueList.enqueue(78)
    queueList.enqueue(68)
    queueList.enqueue(11)
    queueList.enqueue(85)
    print('List: 34, 45, 22, 78, 68, 11, 85')
    print((queueList.peekFront()))
    print((queueList.peekRear()))
    print('Dequeue queue once')
    print(queueList.dequeue())

main()
