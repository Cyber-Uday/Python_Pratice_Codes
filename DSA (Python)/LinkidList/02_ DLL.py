#DLL doubly linked list >> 
""" 
    Doubly linked list overcome the problem of sll 
    sll will not able to go with backword direction >> 
    but in DLL we have ability to go in backword direction also >> 
    
    But Sll is is use less not like that bcz as compare the doubly linked list 
    sll doing that work but it take time consuming more and less memory as compare to the DLL
    
    but in dll prv node will store the address but it take one more varible in every node
    so it takle more space and less time as compare to sll 
    
"""
#q1 define a class Node to create simple node 
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

#q2 : difine a class DLL to implemnet DLL with __init__() method to create initialise start refrence variable

class DLL:
    def __init__(self,start=None):
        self.start=start
        
    #q3 define a methos is_empty to check the DLL IS EMPTY OR NOT 
    def is_empty(self):
        return self.start==None #here we are return the none if dll is empty
    
    def insert_at_start(self,data):
        #create n = Node obj and assign None = prev , data = item , self .start =next 
        n=Node(None,data,self.start)#possiblity  come's which mean >> 
        #if list is empty so koi baat nahi self.start may none ajta >>
        if not self.is_empty():
            self.start.prev=n
        self.start=n
        
    def insert_at_last(self,data):
        temp=self.start
        if self.start !=None:
            while temp is not None:
                temp=temp.next
        n=Node(temp,data,None)#here we give temp bcz if only one node in that case also suit 
        #it will add as a temp =none and last may to none pahije karan list la empty dakhvna asel ..!
        if temp==None:
            self.start=n
        else:
            temp.next=n
    
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None 
                        #here temp bcz te sapdun anel search madhun konta data tr
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            #now we are ready to add this node in the list >> 
            #again we need to do manipulation for this
            if temp.next !=None:
                temp.next.prev=n
            temp.next=n
            
    #q8 print the list >> 
    def Print_List(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
        
    #q9 Delete First Node: 
    def delete_first(self):
        if self.start !=None:
            self.start=self.start.next
            if self.start!=None:
                self.start.prev=None
    
    #10 Delte Last Node :
    def delete_last(self):
        if self.start==None:
            pass
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.prev.next=None
    #q11 delete item
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next    
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self,start):
        self.current=start
    #just return the self 
    def __iter__(self):
        return self
    #imp bcz acutally this will return the valus 
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data 
MyList=DLL()
MyList.insert_at_last(30)
MyList.insert_at_start(20)
MyList.insert_at_start(44)
MyList.insert_after(MyList.search(20),60)
for x in MyList:
    print(x,end=' ')
print()

