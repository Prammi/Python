#max sum of path in a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root=TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

maxSum=[0]
finalTree=[0,0,0]
finalTree[0]=root.val
def getMaxSumPath():
    
    def recurMaxSumPath(node,temp):
        if(node.left and node.right):
            left=recurMaxSumPath(node.left,temp)
            right=recurMaxSumPath(node.right,temp)
            temp=node.val+ max(left,right)             
            finalTree[1]= left
            finalTree[2]=right
            maxSum[0]=max(maxSum[0],temp)   
            return temp 
        elif (node.left):
            temp=node.val+ max(recurMaxSumPath(node.left,temp),0)
            maxSum[0]=max(maxSum[0],temp)
            return temp
        elif(node.right):
            temp=node.val+ max(recurMaxSumPath(node.right,temp),0)  
            maxSum[0]=max(maxSum[0],temp)
            return temp 
        else:
            temp=node.val
            maxSum[0]=max(maxSum[0],temp)
            return temp
    recurMaxSumPath(root,0)

getMaxSumPath()
tempSum=0

if(finalTree[0]>0):
    tempSum=tempSum+finalTree[0]
    if(finalTree[1]>0):
        tempSum=tempSum+finalTree[1]
    if(finalTree[2]>0):
        tempSum=tempSum+finalTree[2]
else:
    if(finalTree[1]>0 and finalTree[2]>0):
        tempSum=tempSum+max(finalTree[1],finalTree[2])
    elif finalTree[1]<0 and finalTree[2]<0:
        tempSum=tempSum+min(finalTree[2],finalTree[1],finalTree[0])
    elif finalTree[1]<0:
        tempSum=tempSum+finalTree[2]
    else:
        tempSum=tempSum+finalTree[1]
        
        
print(tempSum)
        