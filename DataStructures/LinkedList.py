class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        print(f"======Creating a Node with {value}========")
        node=Node(value)
        self.head=node  
        self.tail=node
        self.length=1

    def print_linkedList(self):
        print("======Printing my Linked List========")
        if(self.length==0):
            print("The length of linked list is zero 0 ")
        else:
            temp=self.head
            while temp is not None:
                print(temp.value)
                temp=temp.next

    def append(self,value):
        print(f"======Appending {value} to  Linked List========")

        node = Node(value)

        if(self.head is None):
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        
        self.length+=1       

    def pop(self):
        print("======Popping Last from  Linked List========")
        if(self.length==0):
            print("Nothing left to pop")
        elif(self.length==1):
            self.head=None
            self.tail=None
            self.length=0
        else:
            for i in range(0,self.length-1):
                # print("self.length=" + str(self.length))
                temp=self.head
                if(i==self.length-2): 
                    # print("i="+str(i))               
                    temp.next=None
                    self.tail=temp
                    self.length=self.length-1
                temp=temp.next;  
    
    def prepend(self,value):
        node=Node(value)
        if(self.length !=0):
            node.next=self.head
            self.head=node 
        else:
            self.head=node
            self.tail=node
        self.length+=1

    def popfirst(self):
        if(self.length==0):
            #do something;
            print("No items present for popping")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.length-=1
            if(self.length==0):
                self.head=None
                self.tail=None

my_linkedList=LinkedList(1)
my_linkedList.append(2)
my_linkedList.print_linkedList()

my_linkedList.pop()
my_linkedList.print_linkedList()

my_linkedList.prepend(3)
my_linkedList.print_linkedList()

my_linkedList.popfirst()
my_linkedList.popfirst()
my_linkedList.print_linkedList()


my_linkedList.prepend(3)
my_linkedList.print_linkedList()
