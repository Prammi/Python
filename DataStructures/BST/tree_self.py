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
