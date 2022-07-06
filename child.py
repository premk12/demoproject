from parent import Parent


class Child(Parent):
    num=200
    def __init__(self):
        Parent.__init__(self,2,4)

    def summation1(self):
        return self.firstno+self.secno+self.num+Parent.num+self.summation()
obj=Child()

print(obj.summation1())




