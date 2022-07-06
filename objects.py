# ### Function approach  ## Without class

# id = 1001     # variable
# name = 'Abhijt'   # variable
# address = "Pune"
# salary = 3000000


# def getEmployeeDetails():     #fuction defination 
#     print(f"Employee details : id = {id}, name = {name}, address = {address}, salary = {salary}" )


# getEmployeeDetails()      # function call
# getEmployeeDetails()
# getEmployeeDetails()
# id = 2000
# getEmployeeDetails()
# getEmployeeDetails()


# #### -------------------------------------------------------------------------------------


class Employee:
    id = 1001       ## attribute
    name = 'Abhijt'
    address = "Pune"
    salary = 3000000

    def getEmployeeDetails(self):   # method
        print(f"Employee details : id = {self.id}, name = {self.name}, address = {self.address}, salary = {self.salary}" )

    def getComapanyDetails():   # method
        print("Company Credence is located at Pune and Mumbai...")


##getEmployeeDetails()        # we can not call class method directly outside without class name or object

#Employee.getEmployeeDetails()   # TypeError: getEmployeeDetails() missing 1 required positional argument: 'self'
Employee.getComapanyDetails()

emp = Employee() 
Employee.getEmployeeDetails(emp)

