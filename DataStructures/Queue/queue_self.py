class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue():
    def __init__(self):
        self.length=0
        self.top=None
        self.bottom=None
    
    def push(self,value):
        node=Node(value)
        if self.length==0:
            self.top=node
            self.bottom=node
        else:
            node.next=self.top
            self.top=node
        
        self.length+=1
        
    def pop(self):
        if(self.length==0):
            print("ntn to pop")
        elif(self.length==1):
            self.top=None
            self.bottom=None
            self.length=0
        else:
            temp=self.top
            for i in range(self.length-1):
                if i==self.length-2:
                    temp.next=None
                    self.bottom=temp                
                temp=temp.next
            
            self.length-=1
            
        
    def __str__(self):
        temp=self.top
        while temp is not None:
            print(temp.value.upper())
            print("|")
            temp=temp.next
        print("None")
        return ""
        
q=Queue()
_array =['a','b','c','d','e','f','g']
for i in _array:
    q.push(i)

print(q)

q.pop()
print(q)
            
            
        
