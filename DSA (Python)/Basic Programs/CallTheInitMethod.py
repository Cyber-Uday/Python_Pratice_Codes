#here we are going to call the init method implictly withou tcalling :

class Stud:
    def __init__(self) -> None:
        print("HELO THIS WILL CALLED AUTOMATICALLY..!")
        
    def add(self):
        a=10
        b=2
        print("THE ADDITION IS:> ",(a+b))

obj=Stud()
obj.add()