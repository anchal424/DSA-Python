import sys
class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5
    def is_full(self):
        if self.top==self.CAPACITY-1:
            return True
        else:
            return False
    def push(self,ele):
        if self.is_full():
            print("Stack is full")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele,"is pushed")

    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele=self.stack[self.top]
            self.stack.pop()
            self.top=-1
            return ele
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]
        print("stack is full")
            
if __name__ == '__main__':
    obj=Stacks()
    while True:
        print("1. push")
        print("2. pop")
        print("3. traverse")
        print("4. peek")
        print("5. exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            ele=int(input("Enter data: "))
            obj.push(ele)
        elif ch==2:
            ele=int(input("Is popped: "))
            obj.pop()
        elif ch==3:
            obj.traverse()
        elif ch==4:
            obj.peek()
        elif ch==0:
            sys.exit()    