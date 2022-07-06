class Train:
    def __init__(self,name,seats,fare,person):
        self.name=name
        self.seats=seats
        self.fare=fare
        self.person=person

    def getinfo(self):
        print(f"Train name is  {self.name}")
        print(f"Seats availabel {self.seats}")
        print(f"Fare of seats {self.fare}")

    def ticket_book(self):
        if (self.seats>0):
            print("Ticket booking is succesful")
            self.seats = self.seats-1
            print(f"Seats availabel {self.seats}")
        else:
            print("Seats are not available")

    def Fare_Ticket_discount(self):
        self.fare = self.fare / 1.1
        if(self.fare<720):

            print("You are eligible for offer")

            print(f"Fare of your ticket after 10per discount {(self.fare)}")

        else:
            print("You are not applicable for discoun")


    def booking_person(self):
        if 






    # def quantity_booking(self):
    #     if self.



obj=Train("maharastraexp",56,720,1)

obj.getinfo()

obj.ticket_book()

obj.Fare_Ticket_discount()
