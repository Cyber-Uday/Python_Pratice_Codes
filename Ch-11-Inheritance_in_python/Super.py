#super function help us to acess the diff function from base classes 
# syntax ::  super().Method/Function name

class Emp1:
    def __init__(self):
        print("Emp 1 constructor called")
    print("EMP 1")
    
class Emp2(Emp1):
    print("EMP 2 ")
    def __init__(self):
        super().__init__()
        print("EMO 2 constructor Called")
        
class Emp3(Emp2):
    print("HERE ARE ALL :> ")
    def __init__(self):
        super().__init__()
        print("EMP 3 COnstructor called ")
        
obj=Emp3()
#checch this we need to do this obj()
print(obj)