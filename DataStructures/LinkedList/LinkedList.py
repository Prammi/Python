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
            _str=""
            temp=self.head
            while temp is not None:
                _str=_str+" "+str(temp.value)
                temp=temp.next
            print("[ "+ _str +" ]")
    
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
            prev=self.get(self.length-2)
            prev.next=None
            self.tail=prev
            self.length-=1
    
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
    
    def get(self,index):
        temp=self.head
        for i in range(0,self.length):
            if(i==index):
                #do something;
                return temp
            temp=temp.next
    
    def set(self,index,value):
        temp=self.head
        for i in range(0,self.length):
            if(i==index):
                #do something;
                temp.value=value
            temp=temp.next

    def insert(self,index,value):
        node= Node(value)
        if(self.length==0):
            self.prepend(value)
        elif self.length==index+1:
            self.append(value)
        else:
            if index+1<=self.length:
                prev=self.get(index-1)
                temp=prev.next
                prev.next=node
                node.next=temp
            # current=self.head
            # 
            #     for i in range(0,self.length):
            #         print("i "+str(i))
            #         if(i==index):
            #             temp=current.next
            #             current.next=node
            #             node.next=temp
            #             print(current.next.value)
            #             break
            #         else:
            #             current=current.next
            #         self.length+=1
            else:
                print(f"illegal operation as index {index} > length {self.length}")
        
    def remove(self,index):
        if index==0:
            self.popfirst()
        elif index+1==self.length:
            self.pop()
        else:
            prev=self.get(index-1)
            current=self.get(index)
            prev.next=current.next
            current.next=None
            self.length-=1    

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
        
        
    def swapValues(self,i,j):
        ith=self.getValueatanIndex(i)
        jth=self.getValueatanIndex(j)
        
        ith.value,jth.value=jth.value,ith.value

    def __str__(self):
        start=self.head
        _str=''
        for _ in range(self.length):
            _str=_str+ str(start.value) +'->'
            start=start.next
        
        return _str + 'None'
    
        


# my_linkedList=LinkedList(1)
# my_linkedList.append(2)
# # my_linkedList.print_linkedList()

# my_linkedList.pop()
# # my_linkedList.print_linkedList()

# my_linkedList.prepend(-1)
# # my_linkedList.print_linkedList()

# my_linkedList.append(3)
# my_linkedList.append(4)
# my_linkedList.append(5)
# # my_linkedList.print_linkedList()
# print("The value of LinkedList at index 2 is "+ str(my_linkedList.get(2).value))

# my_linkedList.set(0,-2)
# my_linkedList.print_linkedList()

# my_linkedList.insert(0,-3)
# my_linkedList.print_linkedList()

# my_linkedList2=LinkedList(1)
# my_linkedList2.insert(0,2)
# my_linkedList2.append(3)
# my_linkedList2.append(4)
# my_linkedList2.remove(1)
# my_linkedList2.print_linkedList()

# my_linkedList2.reverse()
# my_linkedList2.print_linkedList()



_array=[1,2,3,4,5]

_linkedList=LinkedList()

for i in _array:
    _linkedList.append(i)
print(_linkedList)

_linkedList.reverseValues(1,3)
print(_linkedList)








