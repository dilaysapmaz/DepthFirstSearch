#Tree DFS search algorithm with preorder way

#Node class. A tree has root, left child, right child and the value.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        # First the root
        print(root.val),
        # Second, call left child with recursion
        printPreorder(root.left)
        # Third, call right child with recursion
        printPreorder(root.right)

# These are the node values for tree. You can change it.
root = Node(5)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(7)
root.left.right = Node(4)
print "Preorder traversal of binary tree is"
#After all, this is the conclusion of the preorder DFS
printPreorder(root)
