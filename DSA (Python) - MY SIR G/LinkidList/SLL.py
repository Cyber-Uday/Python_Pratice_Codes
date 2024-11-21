'''Singly linked list '''
#linear data structure >> where each element has 2 filed 
#one is data(item) and one is next as pointer address>> 

class Node:
                        #we create here local variable which is item and next for node initlize
    def __init__(self,item=None,next=None):
        #now we need to create instance variables object 
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start
    
    def array(self,data):
        self.data=data
        print(f"This is data :> {data}")
        
    def is_empty(self):
        return self.start==None # this way we can check the empty or not >> 
    #  or return True

    #Question 4th is define method insert_at_start to insert an elemenet at starting 
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
        
    #question 5th is define method insert_at_last to insert an element at last >> 
    def insert_at_last(self,data):
        n=Node(data)
            #we checking here list is empty or not 
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n 
            
    #question 6th Is define a method search() to find the node with sepcific element value
    def search(self,data):
        temp =self.start
        #while loop for to check temp unitil the last node
        while temp is not None:
            if temp.item==data:  # if our data will be match then we return that value 
                return temp
            temp=temp.next
        return None #if any node not match then reuturn none
    
    #q7 here we need to add our node after the temp or any perticular node 
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    #q8 here we need to print all the List with implemnet up 
    def print_list(self):
        temp=self.start # bcz we are going to be start from starting right>>
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    
    #9 iterator concept
    
    #10 delete the first node >> 
    def delete_frist(self):#here we get self 
        if self.start is not None:# until the self of next ref not get none 
            self.start=self.start.next
            
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp= temp.next 
            temp.next=None
            
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
            else:
                temp =self.start
                if temp.item==data:
                    self.start=temp.next
                else:
                    while temp.next is not None:
                        if temp.next.item==data:
                            temp.next=temp.next.next 
                            break
                        temp=temp.next
                
            
            
            
#driver code:: 
MyList=SLL()
MyList.insert_at_start(20)
MyList.insert_at_start(50)
MyList.insert_at_start(10)
MyList.insert_at_last(30) 
MyList.insert_after(MyList.search(20),25)
MyList.print_list()
print()
MyList.delete_last()
MyList.delete_last()
MyList.print_list()