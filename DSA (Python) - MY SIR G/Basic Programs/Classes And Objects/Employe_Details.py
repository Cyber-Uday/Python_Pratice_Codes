#here we are going to add the emp name , emp id and emp sal ;

class Emp:
    
    def Emp_name(self,name=None):   
        self.name=name
    
    def Emp_ID(self,id=None):
        self.id=id
        
    def Emp_Sal(self,sal=None):
        self.sal=sal
        

    obj=Emp('uday',3,1000)
    
    print(obj.Emp)
        