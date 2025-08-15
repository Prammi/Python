class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinarySearchTree:
    def __init__(self):
        self.root=None
        
    def addNode(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        else:
            temp=self.root            
            while(True):            
                if new_node.value<temp.value:
                    if temp.left is None:
                        temp.left=new_node
                        return False    
                elif new_node.value>temp.value:
                    if temp.right is None:
                        temp.right=new_node
                        return False
                    
                if value<temp.value:
                    temp=temp.left
                else:
                    temp=temp.right                

    def DFS_PreOrder_Rec(self,node):
        if node is not None:
            print(node.value)
            self.DFS_PreOrder_Rec(node.left)
            self.DFS_PreOrder_Rec(node.right)
        
    def DFS_PreOrder(self):
        temp=self.root
        self.DFS_PreOrder_Rec(temp)
        

    def DFS_InOrder_Rec(self,node):
        if node is not None:
            self.DFS_InOrder_Rec(node.left)
            print(node.value)
            self.DFS_InOrder_Rec(node.right)

    def DFS_InOrder(self):
        temp=self.root
        self.DFS_InOrder_Rec(temp)
        
    def DFS_PostOrder_Rec(self,node):
        if node is not None:
            self.DFS_PostOrder_Rec(node.left)
            self.DFS_PostOrder_Rec(node.right)
            print(node.value)

    def DFS_PostOrder(self):
        temp=self.root
        self.DFS_PostOrder_Rec(temp)
        
                
        

bst=BinarySearchTree()
bst.addNode(4)
bst.addNode(2)
bst.addNode(6)
bst.addNode(1)
bst.addNode(3)
bst.addNode(5)
bst.addNode(7)
print("DFS PRE ORDER")
bst.DFS_PreOrder()
print("DFS IN ORDER")
bst.DFS_InOrder()
print("DFS POST ORDER")
bst.DFS_PostOrder()