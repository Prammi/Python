class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack():
    def __init__(self):
        self.length=0
        self.top=None

    def push(self,value):
        node=Node(value) 
        if self.length==0:
            self.top=node
        else:
            node.next =self.top
            self.top=node
        self.length+=1
            
    def __str__(self):
        temp=self.top
        while temp is not None:
            print(temp.value.upper())
            print("|")
            temp=temp.next
        print("None")
        
        return ""
    
    def pop(self):
        temp=self.top.next
        self.top=temp
        
stack=Stack()
_array =['a','b','c','d','e','f','g']
for i in _array:
    stack.push(i)
stack.pop()            
print(stack)
            