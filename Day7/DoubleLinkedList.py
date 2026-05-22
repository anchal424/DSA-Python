# Double Linked List Menu Driven

import sys

class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None


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

            while ptr.right != None:
                ptr=ptr.right

            ptr.right=newnode
            newnode.left=ptr

        print(data,"is added")

    def traverse(self):

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr=self.head

            while ptr != None:
                print(ptr.data,"->",end=" ")
                ptr=ptr.right

            print("None")

    def addbegin(self):
        data=int(input("Enter data: "))
        newnode=Node(data)

        if self.head is None:
            self.head=newnode

        else:
            ptr=self.head
            newnode.right=ptr
            ptr.left=newnode
            self.head=newnode
            print(data,"is added at beginning")

    def addatbetween(self):
        data=int(input("Enter data: "))
        key=int(input("Enter key: "))

        newnode=Node(data)

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr=self.head

            while ptr != None and ptr.data != key:
                ptr=ptr.right

            if ptr is None:
                print("Key not found")

            else:
                newnode.right=ptr
                newnode.left=ptr.left

                if ptr.left is not None:
                    ptr.left.right=newnode

                ptr.left=newnode

                if ptr == self.head:
                    self.head=newnode

                print(data,"is added at between",key)

    def delete(self):
        key=int(input("Enter key to delete: "))

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr=self.head

            while ptr != None and ptr.data != key:
                ptr=ptr.right

            if ptr is None:
                print("Key not found")

            else:
                if ptr.left is not None:
                    ptr.left.right=ptr.right

                if ptr.right is not None:
                    ptr.right.left=ptr.left

                if ptr == self.head:
                    self.head=ptr.right

                print(key,"is deleted") 

    def deleteatbeginning(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            ptr=self.head
            ptr=ptr.right
            ptr.left=None
            self.head=ptr
            print(ptr.data,"is deleted from beginning") 

    def deleteatbetween(self):
        key=int(input("Enter key to delete: "))

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr=self.head

            while ptr != None and ptr.data != key:
                ptr=ptr.right

            if ptr is None:
                print("Key not found")

            else:
                if ptr.left is not None:
                    ptr.left.right=ptr.right

                if ptr.right is not None:
                    ptr.right.left=ptr.left

                print(key,"is deleted from between")
if _name_ == '_main_':

    obj=DoubleLinkedList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at beginning")
        print("4. Add at between")
        print("5. Delete")
        print("6. Delete at beginning")
        print("7. Delete at between")
        print("0. Exit")

        ch=int(input("Enter your choice: "))

        if ch == 1:
            obj.append()

        elif ch == 2:
            obj.traverse()

        elif ch == 3:
            obj.addbegin()

        elif ch == 4:
            obj.addatbetween()
        elif ch == 5:
            obj.delete()
        elif ch == 6:
            obj.deleteatbeginning()
        elif ch == 7:
            obj.deleteatbetween()
        elif ch == 0:
            sys.exit()