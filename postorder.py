#Tree DFS search algorithm with postorder way

#Node class. A tree has root, left child, right child and the value.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        # First the left child
        printPostorder(root.left)
        # Second, right child
        printPostorder(root.right)
        # Third root
        print(root.val),

# These are the node values for tree. You can change it.
root = Node(5)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(7)
root.left.right = Node(4)
print "Postorder traversal of binary tree is"
#After all, this is the conclusion of the preorder DFS
printPostorder(root)
