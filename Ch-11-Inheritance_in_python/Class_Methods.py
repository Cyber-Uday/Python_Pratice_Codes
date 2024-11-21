#we are learn the class Decorator and class methods>>

class Employee:
    
    a=10
    
    @classmethod
    def show(cls):
        print(f"THIS IS CLASS METHOD: {cls.a}")
        
e = Employee()
e.a = 40
e.show()