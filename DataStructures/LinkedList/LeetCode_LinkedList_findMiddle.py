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

    def find_middle_node(self):
        slowNode = self.head
        fastNode = self.head

        # Traverse the list
        while fastNode is not None and fastNode.next is not None:
            slowNode = slowNode.next
            fastNode = fastNode.next.next

        return slowNode
            



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print( my_linked_list.find_middle_node().value )


