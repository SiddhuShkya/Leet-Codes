# Definition for a binary tree node.
class BinaryTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

    
tree = BinaryTree(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)