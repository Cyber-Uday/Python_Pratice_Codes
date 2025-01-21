#init is an special member function , it take compulsaru minimum one argument as self 
#while we are creating the instace object of the init method it will called automatically

class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a+b)
        
    def multiplaction(self,a,b):
        self.a=a
        self.b=b
        print(a*b)

obj_test=Test(10,30)
obj_2=Test(30,40)

obj_test.multiplaction(5,4)