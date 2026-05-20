import sys
class Stacks:
    def push(self):
        pass
    def pop(self):
        pass
    def traverse(self):
        pass
    def peek(self):
        pass

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
            obj.pop()
        elif ch==3:
            obj.traverse()
        elif ch==4:
            obj.peek()
        elif ch==0:
            sys.exit()