class Hospital:
    hospital_Name:"Drusti Eye Care"
    address="At: Bhajepar ,Po: Wadegaon, Ta:Tirora, Dist:Gondia"

    def __init__(self,name,doctor_name,diases,date,admit_time,paddress,bill):
        self.name=name
        self.doctor_name=doctor_name
        self.diases=diases
        self.date=date
        self.admit_time=admit_time
        self.paddress=paddress
        self.bill=bill

    def VISITOR(self):
        print(f"Patient Detail-----------------")
        print(f"Name of Patient :- {self.name}")
        print(f"Doctor Name :- {self.doctor_name}")
        print(f"Disease Name :- {self.diases}")
        print(f"Patient Adress :- {self.paddress}")
        print(f"Date of Admit :- {self.date}")

    def ACCOUNT(self):
        print(f"Account Details------------")
        print(f"Bill Amount :- {self.bill}")
pname=input("Name of Patient :-")
pdes=input("Disease Name :-")
padd=input("Patient Adress :-")
ptime=input("Time of Admit :-")
pdate=input("Date of Admit :-")
pbill=input("Bill Amount :-")


obj=Hospital(pname,"Manoj pardhi",pdes,pdate,ptime,padd,pbill)

# name,doctor_name,diases,date,admit_time,paddress,bill
obj.VISITOR()

obj.ACCOUNT()




