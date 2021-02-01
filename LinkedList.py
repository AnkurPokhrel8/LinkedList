# -*- coding: utf-8 -*-
"""
@author: Ankur Pokhrel
"""

class Node:                   # Node class 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:               # Linkedlist class
    def __init__(self):
        self.head = None
        
    def addNode(self, data):
        if not self.head:              # if linked list is empty, set first element as head
            self.head = Node(data)
        else:
            top = self.head           # if not, add element at last of linked list
            while top.next:
                top = top.next
            top.next = Node(data)
    def deleteNodefromFirst(self):    
        print(self.head.data, " is deleted")
        self.head = self.head.next                # set second element as head of linkedlist, hence deleting first element
        
    def deleteNodefromLast(self):
        top = self.head
        while top.next.next:
            top = top.next
        print(top.next.data, " is deleted")
        top.next = None                          # set next value of second last element as None, hence deleting last element
        
    def showAll(self):
        top = self.head
        if self.head:
            top = self.head
            while top.next:                     # Iterating through the linkedlist printing all elements
                print(top.data)
                top = top.next
            else:
                print(top.data)
        else:
            print("The Linked List is empty")
            
ll = LinkedList()

ll.addNode(25)
ll.addNode(36)
ll.addNode(5)
ll.addNode(15)
ll.addNode(250)
ll.addNode(360)
ll.addNode(50)
ll.addNode(100)

ll.showAll()

ll.deleteNodefromFirst()
ll.deleteNodefromLast()

ll.showAll()

'''
Output:
    25
    36
    5
    15
    250
    360
    50
    100
    25  is deleted
    100  is deleted
    36
    5
    15
    250
    360
    50
'''
                

        