class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class BST():
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        node=Node(value)
        if self.root is None:
            self.root=node
        else:
            temp =self.root
            while(True):
                if value<temp.value:
                    if temp.left is None:
                        temp.left=node
                        return False
                    temp=temp.left
                elif value>temp.value:
                    if temp.right is None:
                        temp.right=node
                        return False
                    temp=temp.right
    
    def recursiveContains(self, value, nodeValue):
            if nodeValue is None: 
                return False
            elif nodeValue.value==value:
                return True
            else:
                if nodeValue.value < value:
                    return self.recursiveContains(value,nodeValue.right)
                elif nodeValue.value > value:
                    return self.recursiveContains(value,nodeValue.left)
                
    def contains(self,value):
        if self.root is None:
            print("empty tree")
        else:
            temp=self.root
            if value==temp.value:
                return True
            else:
                while temp is not None:
                    if value< temp.value:
                        if temp.left is None:
                            return False
                        else:
                            if value>temp.left.value:
                                temp=temp.right
                            elif value>temp.left.value:
                                temp=temp.left
                            else:
                                return True
                   
                    elif value> temp.value:
                        if temp.right is None:
                            return False
                        else:
                            if value>temp.right.value:
                                temp=temp.right
                            elif value<temp.right.value:
                                temp=temp.left
                            else:
                                return True


my_set=set({1,2,3,4,5})
my_dict={"k1":"v1"}
my_tuple=(1,2,3,4)

        
                
         

bst=BST()
bst.insert(15)
bst.insert(7)
bst.insert(22)
bst.insert(16)
bst.insert(14)
print(bst.recursiveContains(100,bst.root))
# print(bst.root.value)
# print(bst.root.right.value)
# print(bst.root.left.value)

# print(bst.root.left.right.value)
# print(bst.root.right.left.value)
print(my_set)
print(my_dict.items())
print(my_tuple)



from collections import defaultdict
anagrams = defaultdict(list)
print(anagrams)




                