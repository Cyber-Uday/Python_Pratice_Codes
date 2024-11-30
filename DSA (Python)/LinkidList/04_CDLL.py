#now we are going for the Explore the Circular Doubly Linked List >> 
#q1 Node Creation Sucessfully DONE>> 
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
#q2 
class CDLL:
    def init(self,start=None):
        self.start=start
    #q3- here we check cdll is empty or not..!
    def is_empty(self):
        return self.start==None
    #q4- insert_at_start and insert a node in CDLL >> 
    def insert_at_start(self,data):
        n=Node(None,data,next)
        if self.is_empty():
            n.next=n
            n.next
            self.start=n
        else:
            