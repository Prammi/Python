class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1
    
    def printLinkedList(self):
        print("******** Printing Linked List ********")
        if(self.length>0):
            result=""
            node=self.head
            while(True):
                result= result+ str(node.value) + '→'
                node=node.next            
                if(node is None):
                    break
                
            result=result+'None'
            print(result)
            
            
    def AddNode(self,value):
        node=Node(value)
        if(self.length==0):
            self.length=1
            self.head=1
            self.tail=1
        else:
            tail=self.tail
            tail.next=node
            self.tail=node
            self.length+=1
            
    def GetAtIthNode(self,i):
        node=None
        if(i<0):
            print("Cannot Return for Negative Values .......Beep")
        elif(i>self.length):
            print("Index out of bound .......Beep")
        elif(i==1):
            node= self.head
        elif(i==self.length):
            node=self.tail
        else:
            node=self.head
            for j in range(0,i-1):
                node=node.next      
        if(node):      
            print(f"The value at {i} node is {node.value}")
    
    def pairwiseSwap(self):
        print("*********** swap started ************")
        node=self.head
        if(self.length==1):
            self.printLinkedList()
        else:
            while(node and node.next):
                node.value,node.next.value=node.next.value,node.value
                node=node.next.next
            self.printLinkedList()
        print("*********** swap ended ************")
    
    def removeDuplicates(self):
        node=self.head
        while node.next is not None:
            if node.value==node.next.value:
                node.next=node.next.next
            else:
                node=node.next
        
            

              

ll=LinkedList(1)
ll.AddNode(1)
ll.AddNode(1)
ll.AddNode(2)
ll.AddNode(2)
ll.printLinkedList()
ll.removeDuplicates()
ll.printLinkedList() 
ll.pairwiseSwap()
ll.GetAtIthNode(1)   

 