class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(current, key):
            if current is None:
                return Node(key)
            if key < current.key:
                current.left = _insert(current.left, key)
            else:
                current.right = _insert(current.right, key)
            return current

        self.root = _insert(self.root, key)

    def preOrder(self,node):
        if node is not None:            
            print(node.key)
            self.preOrder(node.left)
            self.preOrder(node.right)
        
    def inOrder(self,node):
        if node is not None:            
            self.inOrder(node.left)
            print(node.key)
            self.inOrder(node.right)
            
    def postOrder(self,node):
        if node is not None:            
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.key)
    
    def BfsTraversal(self,node):
        queue=[]
        if node is not None:
            queue.append(node)
            
        while len(queue)>0:
            print(queue[0].key)
            if queue[0].left is not None:
                queue.append(queue[0].left)
            if queue[0].right is not None:
                queue.append(queue[0].right)
            queue.pop(0)
            
    
    def printAllPath(self,root): 
        def printSinglePath(node,path,paths):
            if node is None:
                return
            
            path=path + str(node.key)
            
            if node.left is None and node.right is None:
                paths.append(path)
                
            else:
                path=path+"-->"
                printSinglePath(node.left,path,paths)
                printSinglePath(node.right,path,paths)
                
                

        paths=[]
        printSinglePath(root,"",paths)
        return paths
     
    def printAllLeft(self,root):
        
        def getLeftPath(node,path):
            if node is None:
                return ""
            
            path=path+str(node.key)
            if node.left is None:
                return path
            else:
                path=path+'==>'
                return getLeftPath(node.left,path)
                
        
        path=""
        return getLeftPath(root,path)
    
    
    def getKthElement(self,root):
        
        def formArrayfromBST(node,result):
            if node is None:
                return None
            formArrayfromBST(node.left,result)
            result.append(node.key)
            formArrayfromBST(node.right,result)
            
        
        result=[]
        formArrayfromBST(root,result)
        return result
    
    def bfs_printnodeSet(self,root):
        from collections import deque
        queue=deque()
        result=[]
        result.append([root.key])
        queue.append(root)
        while len(queue)>0:
            temp=[]
            if queue[0].left:
                temp.append(queue[0].left.key)
                queue.append(queue[0].left)
            if queue[0].right:
                temp.append(queue[0].right.key)
                queue.append(queue[0].right) 
            if len(temp)>0:
                result.append(temp)            
            queue.popleft()         
        return result    
            
                
                
                

            
                
        
# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
print("Pre Order")
bst.preOrder(bst.root)
print("in Order")
bst.inOrder(bst.root)
print("Post Order")
bst.postOrder(bst.root)
print("bst traversal")
bst.BfsTraversal(bst.root)
print("printing all paths")
paths=bst.printAllPath(bst.root)
print(paths)
lPath=bst.printAllLeft(bst.root)
print(lPath)
KthValue=2
result=bst.getKthElement(bst.root)
print("The "+str(KthValue)+" in the BST is "+str(result[KthValue-1]))
print("printing BFS node list ")
result=bst.bfs_printnodeSet(bst.root)
print(result)

