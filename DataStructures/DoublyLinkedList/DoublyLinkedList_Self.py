class Node():
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None
        
class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def appendNode(self,value):        
        node=Node(value)
        if(self.length==0):
            self.head=node
            self.tail=node
        else:            
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
        self.length+=1
        
    def __str__(self):
        temp=self.head
        str=""
        while temp is not None:
            str=str+ temp.value +" <--> "
            temp=temp.next
        
        return str +"None"
    
    def pop(self):
        self.tail=self.tail.prev
        self.tail.next=None
    
    def popatIndex(self,i):
        temp=self.get(i)
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
        
    
        
    def get(self,index):
        temp=self.head
        for i in range(self.length):
            if i==index:
                req=temp
                return req            
            temp=temp.next   
            
    def reverseLinkedList(self):
       current=self.head
       prev=None
       while current:
           temp=current.next
           current.next=prev
           current.prev=temp
           prev=current
           current=current.prev
       self.head=prev
          

dd=DoublyLinkedList()
_array =['a','b','c','d','e','f','g']
for i in _array:
    dd.appendNode(i)

dd.pop()
# print(dd)   
dd.popatIndex(2)
# print(dd)   
print(dd.get(1).value)
# print(dd)            
dd.reverseLinkedList()
print(dd)   
