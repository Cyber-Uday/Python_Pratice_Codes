#in multilevel Inheritance we can create a another derivied class from derivied class >> 

class A:
    print("I AM CLASS A")

class B(A):
    print("I AM CLASS B")

class C(B):
    print(" I AM CLASS C")
    
obj=C()
print(obj)

#this way we can done the multilevel inheritance 