#here we are going to explore the init function and lot of more ..! 

class Employee:
    
    def __init__(self,name):# it does not need to call it will call auto
        self.name=name
        print(f"HELLOW {self.name}")
        
    #here wee need to call this function
    def Display_Data(self,string):
        self.string=string
        print(f"The name is :> {self.string}")
        
    @staticmethod
    def Display_data_2(string):
        print(f"2nd name is :> {string}")
        
Uday = Employee("HACKER")

print(Uday.name)

Uday.Display_Data("Uday")# here we need to call but while we need to declare the init so 
#there will be just object declare we don't need to call it 

Uday.Display_data_2("SOHAM")