class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    def dfs(node, path, paths):
        if node is None:
            return
        path=path+str(node.val)
        if node.left is None and node.right is None:
            result.append(paths)
        else:
            path=path+"-->"
            dfs(node.left,path,paths)
            dfs(node.left,path,paths)
            
        
            
    result = []
    dfs(root, "", result)
    return result




def printAllPath(root):
    
    def printSinglePath(node,path,paths):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            result.append(paths)
            
        else:
            path=path+node.val +"-->"
            printSinglePath(node.left,path,paths)
            printSinglePath(node.right,path,paths)
            
            
    
    result=[]
    printSinglePath(root,"",[])

# Create the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

# Test the function
print(binaryTreePaths(root))

