# Linked list menu driven

import sys
class Getnode:
    def _init_(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def _init_(self):
        self.head=None

    def append(self):
        data=int(input("Enter data: "))
        newnode=Getnode(data)

        if self.head == None:
            self.head=newnode
        else:
            ptr=self.head

            while ptr.next != None:
                ptr=ptr.next

            ptr.next=newnode

        print(data,"is added")

    def traverse(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            ptr=self.head

            while ptr != None:
                print(ptr.data,"->",end=" ")
                ptr=ptr.next

            print("None")

    def addbegin(self):
        data=int(input("Enter data: "))
        newnode=Getnode(data)

        if self.head == None:
            self.head=newnode
        else:
            ptr=self.head
            newnode.next=ptr
            self.head=newnode

        print(data,"is added at beginning")

    def addatbetween(self):
        data=int(input("Enter data: "))
    key=int(input("Enter key: "))

    newnode=Getnode(data)

    if self.head == None:
        print("Linked list is empty")

    else:
        ptr=self.head

        while ptr != None:
            if ptr.data == key:
                break
            ptr=ptr.next

        if ptr == None:
            print("Key is not found")

        else:
            newnode.next=ptr.next
            ptr.next=newnode
            print(data,"is added after",key)

    def deleteatbeginning(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            ptr=self.head
            ptr=ptr.next
            ptr.next=None
            self.head=ptr
            print(ptr.data,"is deleted from beginning")

    def deleteatend(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            ptr=self.head
            while ptr.next != None:
                ptr1=ptr
                ptr=ptr.next

            ptr1.next=None
            print(ptr.data,"is deleted from end")
if _name_ == '_main_':
    obj=LinkedList()

    while True:
        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at beginning")
        print("4. Add at between")
        print("5. Delete at beginning")
        print("6. Delete at end")
        print("7. Exit")

        n=int(input("Enter your choice: "))

        if n==1:
            obj.append()

        elif n==2:
            obj.traverse()

        elif n==3:
            obj.addbegin()

        elif n==4:
            obj.addatbetween()

        elif n==5:
            obj.deleteatbeginning()

        elif n==6:
            obj.deleteatend()

        elif n==7:
            sys.exit(0)