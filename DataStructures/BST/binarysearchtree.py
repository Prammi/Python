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
               
    def contains(self,value):
        if self.root is None:
            return False
        temp=self.root
        while(temp is not None):
            if(temp.value==value):
                return True
            
            if value <temp.value:
                temp=temp.left
            else:
                temp=temp.right                 
        return False
    
    def rContains(self,temp,value):
        if temp is None:
            return False
        if(temp.value < value):
            temp=temp.right
            return self.rContains(temp,value)
        elif temp.value>value:
            temp=temp.left
            return self.rContains(temp,value)                
        else:
            return True
           
    def recursiveContains(self,value):
        temp =self.root
        x=self.rContains(temp,value)
        print("contains---" + str(x) )
    
    def rInsert(self,temp,value):
        if temp is None:
            temp=Node(value)
        else:
            if value<temp.value:
                temp.left=self.rInsert(temp.left,value)
            elif value>temp.value:
                temp.right=self.rInsert(temp.right,value)        
        return temp
        
    def recursiveInsert(self,value):
        return self.rInsert(self.root,value)
    
    def rDelete(self,temp,value):
        if temp is None:
            return None
        else:
            if value<temp.value:
                temp.left=self.rDelete(temp.left,value)
                return temp
            elif value>temp.value:
                temp.right=self.rDelete(temp.right,value)
                return temp
            else: 
                if temp.left is not None:
                    temp=temp.left
                elif temp.right is not None:
                    temp=temp.right
                return temp
            
    def recursiveDelete(self,value):
        return self.rDelete(self.root,value)
    
    def recursiveInsert2(self,value):
        return self.rInsert2(self.root,value)
    
    def rInsert2(self,temp,value):
        if temp is None:
            return Node(value)
        else:
            if value<temp.value:
                temp.left=self.rInsert2(temp.left,value)
                return temp
            elif value>temp.value:
                temp.right=self.rInsert2(temp.right,value)
                return temp
            
    def getMinValueRecursive(self,temp,minValue):
        if temp is None:
            return minValue
        else:
            value=temp.value
            return self.getMinValueRecursive(temp.left,value)
           
    def getMinValue(self):
        print(self.getMinValueRecursive(self.root,0))
    
    def  recursiveInvert(self,temp):
        if temp is None:
            return None
        else:
           temp.left,temp.right=temp.right,temp.left
           self.recursiveInvert(temp.left)
           self.recursiveInvert(temp.right)           
           return temp
    
    def invertBinaryTree(self):
        self.recursiveInvert(self.root)
        
    #Depth first search DFS pre order 
    def traversal(self,currentNode):
        print(currentNode.value)
        if currentNode.left is not None:
            self.traversal(currentNode.left)
        if currentNode.left is not None:
            self.traversal(currentNode.right)

    def DFS_PostOrder(self,currentNode):
        print("# couldnt clear this ")
    
    def DFS_Inorder(self,currentNode,headValue):
        if currentNode.left is not None:
            self.DFS_Inorder(currentNode.left)
        if currentNode.right is not None:
            self.DFS_Inorder(currentNode.right)
        print(currentNode.value)    
        print("# couldnt clear this ")

            
            
    #BReadth first search  BFS
    def breadthFirst(self,temp):
        queue=[]
        queue.append(temp)
        while len(queue) > 0:
            currentNode=queue.pop(0)
            print(currentNode.value)
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
            
            
            
    
            

bst=BinarySearchTree()
bst.addNode(47)
bst.addNode(21)
bst.addNode(76)
bst.addNode(18)
bst.addNode(27)
bst.addNode(52)
bst.addNode(82)
# bst.invertBinaryTree()
# print()
# bst.recursiveInsert(5)
# bst.recursiveContains(47)
# bst.recursiveDelete(25)
# bst.recursiveContains(25)
# bst.getMinValue()

# bst.traversal(bst.root)
# bst.breadthFirst(bst.root)
bst.DFS_PostOrder(bst.root)







