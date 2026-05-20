""" Stack Without Using Capacity. """

import sys

class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, ele):
        self.top = self.top + 1
        self.stack.append(ele)
        print(ele, "is pushed")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top = self.top - 1
            return ele

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]

    def traverse(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])


if __name__ == '__main__':
    obj = Stacks()

    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Traverse")
        print("4. Peek")
        print("5. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            ele = int(input("Enter data: "))
            obj.push(ele)

        elif ch == 2:
            ele = obj.pop()
            if ele is not None:
                print(ele, "is popped")

        elif ch == 3:
            obj.traverse()

        elif ch == 4:
            ele = obj.peek()
            if ele is not None:
                print("Top element is:", ele)

        elif ch == 5:
            sys.exit()            