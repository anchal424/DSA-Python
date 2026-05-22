class A:
    def showA(self):
        print("I am in class A.")
class B(A):
    def showB(self):
        print("I am in class B.")

class C(A,B):
    def showB(self):
        print("I am in class C.")


if __name__ == '__main__':
    obj=C()
    obj.showA()
    obj.showB()
    obj.showC()        

        