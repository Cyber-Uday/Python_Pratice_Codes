#here we are going to explore the Circular Linked List..!

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class CLL:
    def __init__(self,last=None):
        self.last=last
    
    def is_empty(self):
        return self.last==None
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    
    def search(self,data):
        
        if self.is_empty():
            return None
        #here we are going for if node not empty 
        temp=self.last
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
        
    def insert_after(self,temp,data):
        if temp !=None:
            n=Node(data,temp.next)#bcz we need to add new node after temp right 
            temp.next=n
            if temp==self.last:
                self.last=n            
            
    def Print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item)
                temp=temp.next
            print(temp.item)
    
    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
    
    def delete_last(self):
        #traversing needed haye
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next !=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
                
    def delete_item(self,data):
        #case1 List is empty
        if not self.is_empty():
            #case2 only one Node
            if self.last.next==self.last:
                if self.last == data: 
                    self.last=None
                else:
                    #case 4th if first node then 
                    if self.last.next==data:
                        self.delete_first()
                    else:
                        temp=self.last.next
                        while temp!=self.last:
                            #for case 3rd if last node then 
                            if temp.next==self.last:
                                self.delete_last()
                                break
                            if temp.next.item==data:
                                temp.next=temp.next.next
                                break
                            temp=temp.next
    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)

class CLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0 #for using this we check if last node print or not then this use there
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:#this count will help us to achive last one 
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data

cll=CLL()

cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_after(cll.search(10),50)
cll.insert_at_last(40)
cll.delete_first()
cll.Print_list()

print("AFTER RESOLVE:> ")

for x in cll:
    print(x,end=' ')
print()