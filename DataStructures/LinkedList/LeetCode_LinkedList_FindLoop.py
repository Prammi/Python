class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
def find_kth_from_end(my_linked_list,k):
    slow=my_linked_list.head
    fast=my_linked_list.head
    for i in range(0,k-1):
        if(fast is not None and fast.next is not None):
            fast=fast.next
        else:
            return None
    while fast is not None and fast.next is not None:
        fast=fast.next
        slow=slow.next
    return slow  
    
           
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)



print(result.value)  # Output: 4