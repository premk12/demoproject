class Thetre:


    def __init__(self,thetrename, moviename,fare,seat):

        self.thetrename=thetrename
        self.moviename=moviename
        self.fare=fare
        self.seat=seat



    def thetre_info(self):
        print("THETRE NAME:",self.thetrename)
        print("MOVIE NAME:",self.moviename)
        print("MOVIE AMOUNT:",self.fare)
        print("SEAT",self.seat)

    def availablity(self):
        print(f"AVAILABLE SEATS {self.seat}")

    @staticmethod
    def greet():
        print("****Your movie ticket booking information***")


    def seat_book(self):
        if (self.seat>0):
            booking=int(input("QTY OF TICKET:"))
            self.seat = self.seat - booking
            print(f"SEAT AVAILABLE NOW {self.seat}")
            fare1= self.fare * booking
            print(f"TOTAL FARE OF BOOKING  {fare1}")
            if (fare1>=1000):
                print("***CONGRATULATION YOU ARE ELIGIBLE FOR DISCOUNT***")
                discount=fare1*1/10
                print(f"DISCOUNT APPLY AS PER 10% {discount}")
                finalbill=fare1-discount
                print("YOUR BILL AFTER DISCOUNT",finalbill)
                print(f"***CONGRATULATION YOUR TICKET IS BOOKED***")
    @staticmethod
    def booked():
            print("**CANCEL YOUR TICKET***")


    def cancelticket(self):
        cancel = int(input("Ticket Cancel Quantity:"))
        if (self.seat+cancel<=200):
            self.seat=self.seat+cancel
            refundamount=self.fare*cancel
            print(f"YOUR REFUNDABLE AMOUNT:{ refundamount}")

































obj=Thetre("PVR","THOR",350,200)

obj.greet()
obj.thetre_info()
obj.seat_book()
obj.booked()

obj.cancelticket()
obj.availablity()











