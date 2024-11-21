#we are learn the class Decorator and class methods>>
# with we are going with property Decorator's to explore the data abstraction and 
#data encapsulation 

class Employee:
    
    a=10
    
    @classmethod
    def show(cls):
        print(f"THIS IS CLASS METHOD: {cls.a}")
        
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        #we are hide the data from the user and user give only a essential details
        self.fname=value.split(" ")[0] # here the part of encapusulation multiple kama la ek 
                                        #madhe add karun dila means class Employee 
        self.lname=value.split(" ")[1]        
e = Employee()
e.a = 40
e.name="UDAY PAYGHON"
print(e.fname,e.lname)
e.show()