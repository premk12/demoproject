class Bike:
    km=100
    name="splender"
    location="Tirora"

    def __init__(self,company,age):
        self.company=company
        self.age = age

    def bikeinfo(self):
        print(self.km, self.name,self.location)

    def milege(self):
        print("this is good bike")

obj=Bike("hero",10)

obj.bikeinfo()


