""" Reverse an array using Stack. """

import sys

class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 10
        
    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False
        
    def push(self, ele):
        if self.isFull():
            print("stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")
            
    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])
            
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return None
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            return ele
            
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stack[self.top]

if __name__ == '__main__':
    obj = Stacks()
    arr = [234235, 235, 235, 235, 5]

    print("Original array:")
    print(arr)

    for i in range(len(arr)):
        obj.push(arr[i])
    rev = []
    for i in range(len(arr)):
        ele = obj.pop()
        rev.append(ele)

    print("Reversed array: ",rev)       