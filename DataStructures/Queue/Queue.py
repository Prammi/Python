class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Queue:
        def __init__(self,value):
            node=Node(value)
            self.length=1
            self.first=node
            self.last=node
        
        def print_queue(self):
            if self.first is None:
                return None
            else:
                temp=self.first
                while temp is not None:
                    print(temp.value)
                    temp=temp.next  
        
        def enqueue(self,value):
            node=Node(value)
            if self.length==0:
                self.first=node
                self.last=node
            else:
                temp=self.last
                temp.next=node
                self.last=node  
            self.length+=1
            
        def dequeue(self):
            if self.length==0:
                return None
            else:
                if(self.length==1):
                    self.first=None
                    self.last=None
                else:
                    temp=self.first
                    self.first=temp.next
                    temp.next=None
                    self.length-=1
                    if(self.length==1):
                        self.tail=temp
                

q1=Queue(1)
q1.enqueue(2)
q1.dequeue()
q1.print_queue()