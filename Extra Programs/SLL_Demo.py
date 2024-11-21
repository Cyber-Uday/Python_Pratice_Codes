
class Node:
    def __init__(self,item=None,start=None):
            self.item =item
            self.start = start 
            
class SLL:
    
    def __init__(self,data):
        self.data=data
    
    def is_empty(self):
        return self == None
    
    def insert_at_first(self):
        n=Node(self,data,start)
        self.n=n
        
MyList=SLL()
print(MyList)