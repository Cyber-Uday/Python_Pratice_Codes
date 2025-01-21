#here we are going with stack using list >>
#list has some method's which we are using for an perform operation on list 
#append to add , pop to remove and return value, len to find the length >> 
#in python the indexing is there on-going::>> last element index is -1 in pyton neagtive indexing >>

#q1 >> define a class stack and initilize the method init>>

class Stack:
    def __init__(self):
        self.items=[]
    
    #q2 >> define a method is_empty to check the list is empty or not>>
    def is_empty(self):
        return len(self.items)==0
    
    #q3 >> define a method push() to add the element's in the stack list>>
    def push(self,data):
        self.items.append(data)
    
    #q4 >> define a method pop() to delete and saying the which delement is del>>
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("STACK IS EMPTY>>> ")
    
    #q5 define a peek() method to return top element on the stack ..!
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is Empty")
        
    
    def size(self):
        return len(self.items)
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("TOP VALUE OF THE LIST IS :> ",s1.peek())
print("POP ELEMENT IS:> ",s1.pop())
print("After the pop top element is",s1.peek())
print("ALL ELEMENT's ARE:>> ",s1.items())
print("Size of the stack is:> ",s1.size())