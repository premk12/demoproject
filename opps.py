class Employee:
    name = "prem"
    id = 101
    location="pune"

    def details(self):
        print(f"details:name={self.name},id={self.id},location={self.location}")

    def company():
        print(" company name is accenture")


emp = Employee()

Employee.details(emp)  ####class.methodname(objectname)

# emp.details()  ##object.methodname

Employee.company()

emp.id=201
emp.name="daddu"
emp.location="tirora"

Employee.details(emp)


emp2=Employee()

emp2.location="nagpur"

emp2.details()

