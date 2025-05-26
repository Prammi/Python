class Node:
    
        self.value=value
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1

    def print_list(self):
        temp=self.head
        op=''
        while(temp is not None):
            op= op+ ' ' +str(temp.value)
            temp=temp.next

        op='['+ op +' ]'
        print(op)
    
    def append(self,value):
        node=Node(value)

        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
        self.length+=1
    
    def pop_first(self):
        if self.head is None:
            print("No item to Pop")
        else:
            temp=self.head
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
            # temp=self.head.next
            # self.head=temp
            # self.head.prev=None
        self.length-=1
        if(self.length==0):
            self.head=None
            self.tail=None
    
    def pop(self):
        if self.length==0:
            print('Nothing to Pop')
        else:
            temp=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
            temp.next=None
        self.length-=1
        if(self.length==0):
            self.head=None
            self.tail=None
    
    def prepend(self,value):
        node=Node(value)
        if self.length==0:
            self.head=node
            self.tail=node
        else:
            temp=self.head
            node.next=self.head
            self.head.prev=node
            self.head=node
        self.length+=1

    def get(self,index):
        if(index>self.length or index <0):
            print("Index out of bound")
        else:
            i=0
            temp=self.head
            while i<self.length:
                if(i==index):
                    return temp
                i+=1
                temp=temp.next

    def set(self,index,value):
        if(index>self.length or index <0):
            print("Index out of bound")
        else:
            i=0
            temp=self.head
            while i<self.length:
                if(i==index):
                    temp.value=value
                i+=1
                temp=temp.next
    
    def insert(self,index ,value):
        if(self.head is None and index>0):
            print("cannot add to empty list")
        elif(index>self.length):
            print("Index out of bound")
        else:
            if(index==0):
                self.prepend(value)
            elif(index==self.length+1):
                self.append(value)
            else:
                node=Node(value)
                tempNode=self.get(index-1)
                tempNodeNext=self.get(index-1).next
                tempNode.next=node
                node.prev=tempNode
                node.next=tempNodeNext
                tempNodeNext.prev=node
            self.length+=1
            
    def remove(self,index):
        if(self.length==0):
            print("cannot remove from empty ll")
        elif(index>self.length or index<0):
            print("Index out of bound")
        else:
            if(index==0):
                self.pop_first()
            elif(index==self.length-1):
                self.pop()
            else:
                temp=self.get(index)
                prev=temp.prev
                next=temp.next
                prev.next=next
                next.prev=prev
                temp.next=None
                temp.prev=None
                self.length-=1
        
       
                
            
            
dll=DoubleLinkedList(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.print_list()


dll2=DoubleLinkedList(1)
dll2.append(2)
dll2.append(3)
dll2.pop_first()
dll2.print_list()

dll3=DoubleLinkedList(1)
dll3.append(2)
dll3.append(3)
print(dll3.get(2))
print(dll3.get(-1))


dll3=DoubleLinkedList(1)
dll3.append(2)
dll3.append(4)
dll3.print_list()
dll3.set(2,3)
dll3.print_list()


dll4=DoubleLinkedList(1)
dll4.append(2)
dll4.append(4)
dll4.print_list()
dll4.insert(2,3)
dll4.print_list()


dll5=DoubleLinkedList(1)
dll5.append(2)
dll5.append(4)
dll5.append(3)
dll5.print_list()
dll5.remove(2)
dll5.print_list()
dll5.remove(0)
dll5.print_list()
dll5.remove(1)
dll5.print_list()

