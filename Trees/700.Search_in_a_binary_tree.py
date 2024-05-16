"""
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.
"""

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

def searchBST(root, val):
    while root:
        if root.value == val:
            return root
        elif root.value < val:
            root = root.right
        else:
            root = root.left
    return None

print(searchBST(root, 2))