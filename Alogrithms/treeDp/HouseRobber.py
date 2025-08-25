class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# root = TreeNode(3)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(1)

# root=TreeNode(3)
# root.left = TreeNode(4)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(1)

root=TreeNode(5)
root.right = TreeNode(10)
root.right.right = TreeNode(15)


def maxRobbery():
    def recursiveRobber(node,i,total):
        if i%2==0:
            total[0]=total[0] +node.val
        else:
            total[1]=total[1] +node.val
        if(node.left):
            recursiveRobber(node.left,i+1,total)
        if(node.right):
            recursiveRobber(node.right,i+1,total)
    total = [0,0] 
    recursiveRobber(root,0,total)
    return max(total[0],total[1])

print(maxRobbery())

