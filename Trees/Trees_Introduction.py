# Binary Trees in python: Introduction and Traversal Algorithms
from collections import deque

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
    
    def pre_order(self, root):
        stack = [root]
        result = []
        while stack:
            curr = stack.pop()
            result.append(curr.value)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result
    
    def pre_order_recursive(self, root):
        if not root:
            return
        print(root.value) 
        self.pre_order_recursive(root.left)
        self.pre_order_recursive(root.right)

    def in_order(self, root):
        result = []
        if not root:
            return result
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.value)
            curr = curr.right
        return result

    def in_order_recursive(self, root):
        if not root:
            return
        self.in_order_recursive(root.left)
        print(root.value)
        self.in_order_recursive(root.right)

    def post_order(self, root):
        result = deque()
        if not root:
            return result
        stack = [root]
        while stack:
            curr = stack.pop()
            result.appendleft(curr.value)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return result
    
    def post_order_recursive(self, root):
        if not root:
            return
        self.post_order_recursive(root.left)
        self.post_order_recursive(root.right)
        print(root.value)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print("Preorder traversal")
print(tree.pre_order(tree.root))
print(tree.pre_order_recursive(tree.root) )
print("Inorder traversal")
print(tree.in_order_recursive(tree.root) )
print("Postorder traversal")
print(tree.post_order_recursive(tree.root) )
print(tree.post_order(tree.root))

