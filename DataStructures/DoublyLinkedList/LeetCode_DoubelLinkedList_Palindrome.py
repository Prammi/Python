class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def is_palindrome(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            return True
        else:
            left=self.head
            right=self.tail
            while left != right and left.prev==right:
                # left != right  works for odd number of numbner
                # left.prev==right works for even numbers
                # these conditions prevent completing full loop
                if left.value!=right.value:
                    return False
                left=left.next
                right=right.prev
            return True   
        




my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""

