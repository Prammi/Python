class node():
    
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList():
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        _node= node(value)
        if self.head is None:
            self.head=_node
            self.tail=_node
        else:
            self.tail.next=_node
            self.tail=_node
        
        self.length+=1
        
    def __str__(self):
        start=self.head
        _str=''
        for _ in range(self.length):
            _str=_str+ str(start.value) +'->'
            start=start.next
        
        return _str + 'None'
        
    def getValueatanIndex(self,index):
        if self.length==0:
            print("No value to print")
        else:
            temp=self.head
            for i in range(self.length):
                if(i==index):
                    
                    return temp
                else:
                    temp=temp.next
    
    def swapValues(self,i,j):
        first_node=self.getValueatanIndex(i)
        first_node_prev=self.getValueatanIndex(i-1)
        first_node_next=first_node.next
        
        second_node=self.getValueatanIndex(j)        
        second_node_prev=self.getValueatanIndex(j-1)
        second_node_next=second_node.next
        
        first_node_prev.next=None
        first_node_prev.next=second_node
        first_node_prev.next.next=first_node_next
        
        
        second_node_prev.next=None
        second_node_prev.next=first_node
        second_node_prev.next.next=second_node_next
    
    def reverseValues(self,i,j): 
        prev_i=self.getValueatanIndex(i-1)
        next_j=self.getValueatanIndex(j+1)
        
        prev=next_j
        current=self.getValueatanIndex(i)
        for i in range(0,j):
            next=current.next
            current.next=prev
            prev=current
            current=next
            
        prev_i.next=prev
        
_array=[1,2,3,4,5]

_linkedList=LinkedList()

for i in _array:
    _linkedList.append(i)
print(_linkedList)

# _node=_linkedList.getValueatanIndex(1)
# print("value at req index is "+str(_node.value))

# _linkedList.swapValues(1,3)
_linkedList.reverseValues(1,3)
print(_linkedList)
