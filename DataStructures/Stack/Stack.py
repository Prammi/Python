class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Stack:
    def __init__(self,value):
        node=Node(value)
        self.top=node
        self.height=1
     
     
    def print_stack(self):
        temp=self.top
        print("=================")
        while(temp is not None):
            print(temp.value)
            temp=temp.next
        print("=================")
        
    def push(self,value):
        node=Node(value)
        if self.height==0:
            self.top=node
        else:
            node.next=self.top
            self.top=node  
        self.height+=1
        
    def pop(self):
        if self.top is None:
            return None
        else:
            temp =self.top
            next=self.top.next
            self.top=next
            temp.next=None
            self.height-=1

        
        
s1=Stack(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.print_stack()
s1.pop()
s1.print_stack()
print(s1.top.value)
  
        
            
        