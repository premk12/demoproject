class Parent:
    num=100
    def __init__(self,a,b):
        self.firstno=a
        self.secno=b

    def summation(self):
        return self.firstno+self.secno+ Parent.num
obj=Parent(2,3)

print(obj.summation())
