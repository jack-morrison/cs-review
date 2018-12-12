#!/usr/bin/env python3

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# left, root, right
def inOrderTraverse(node):
    if node:
        inOrderTraverse(node.left)
        print(node.val)
        inOrderTraverse(node.right)

# root, left, right
def preOrderTraverse(node):
    if node:
        print(node.val)
        preOrderTraverse(node.left)
        preOrderTraverse(node.right)

# left, right, root
def postOrderTraverse(node):
    if node:
        postOrderTraverse(node.left)
        postOrderTraverse(node.right)
        print(node.val)

root = Node(3)
root.left = Node(1)
root.left.left = Node(5)
root.right = Node(8)
root.right.right = Node(4)
root.right.left = Node(7)

#            3
#          /   \
#         1     8
#        /     / \
#       5     7   4
#
# in-order = 5 1 3 7 8 4
# pre-order = 3 1 5 8 7 4
# post-order = 5 1 7 4 8 3

print("in-Order traversal:")
inOrderTraverse(root)

print("pre-Order traversal:")
preOrderTraverse(root)

print("post-Order traversal:")
postOrderTraverse(root)
