class Node():
    def __init__(self,value):
        self.value=value
        self.bottom=None
        
class Stack():
    def __init__(self):
        self.top=None
        self.length=0
        pass
    
    def push(self,value):
        node=Node(value)
        if(self.length==0):
            self.top=node
        else:
            node.bottom=self.top
            self.top=node
        
        self.length+=1
        
    def printStack(self):
        if self.length>0:
            node=self.top
            while(node):
                print(node.value)
                print("↓")
                node=node.bottom
                
            print("None")
        else:
            print("********* No elements to print ***********")
            
    def pop(self):
        if self.length>0:
            self.top=self.top.bottom
            self.length -= 1

        else:
            print("********* No elements to POP ***********")
    
    def perfectPair(self):
        _dict={"[":"]","{":"}","(":")"}
        if self.length>0:
            i=0
            while i<self.length:
                
                i+=1    
        
        
_stack=Stack()
_stack.push(1)
_stack.push(2)
_stack.push(3)
_stack.push(4)
_stack.push(5)
_stack.pop()
_stack.printStack()


_stack2=Stack()
print(_stack2.perfectPair("[{()}]"))







        