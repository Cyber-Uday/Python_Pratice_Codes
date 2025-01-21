#here we are going to call the init method implictly withou tcalling :

class Stud:
    def __init__(self) -> None:
        print("HELO THIS Init Method WILL CALLED AUTOMATICALLY..!")
        
    def add(self,a,b):
        print("THE ADDITION IS:> ",(a+b))

obj=Stud()
obj.add(5,12)