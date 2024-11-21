#here we are going to explore the multiple inheritance ?>>
#multiple parent but one child
#which means from multiple base class we can create only one derivied class called inheritance >> 

class A:
    print("I AM FROM CLASS A ")
    
class B:
    print("I AM FROM CLASS B ")
    
class C(A,B):
    print("I AM FROM CLASS C")
    
obj=C

print(obj)