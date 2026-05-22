# Implementing Stack using single linked list

import sys
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None

class DoubleLinkedList:
    def _init_(self):
        self.head=None

    def append(self):
        data=int(input("Enter data: "))
        newnode=Node(data)

        if self.head is None:
            self.head=newnode

        else:
            ptr=self.head

            while ptr.next != None:
                ptr=ptr.next

            ptr.next=newnode

        print(data,"is added")

    def traverse(self):

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr=self.head

            while ptr != None:
                print(ptr.data,"->",end=" ")
                ptr=ptr.next

            print("None")

    def peek(self):
        if self.head is None:
            print("Stack is empty")
        else:
            ptr=self.head

            while ptr.next != None:
                ptr=ptr.next

            print(ptr.data,"is peeked")

    def deleteatend(self):
        if self.head is None:
            print("Stack is empty")
        else:
            ptr=self.head
            prev=None

            while ptr.next != None:
                prev=ptr
                ptr=ptr.next

            if prev is not None:
                prev.next=None
            else:
                self.head=None

            print(ptr.data,"is popped") 
if _name_ == '_main_':

    obj=DoubleLinkedList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. Peek")
        print("4. Pop")
        print("0. Exit")

        ch=int(input("Enter your choice: "))

        if ch == 1:
            obj.append()

        elif ch == 2:
            obj.traverse()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.deleteatend()
        elif ch == 0:
            sys.exit()