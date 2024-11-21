#here we  are going to explore the single inheritance 
#using inheritance we can reuse our code >> 
#using inheritance we can access the properties of base class >> 

class Employee:
    print ("Company : GOOGLE ")
    def emp_name(self):
        print(f"THis is the Name of an emp:{self} ")

class Company(Employee):
    print("COMPANY : MICROSOFT ")
    def emp_name(self):
        print(f"THIS IS THE NAME OF AN EMP : {self} ")
    
        
a=Employee
b=Company

print( b.emp_name("UDAY"))