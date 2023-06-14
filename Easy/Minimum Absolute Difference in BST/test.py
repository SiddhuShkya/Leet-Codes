class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

tree = Tree(1)
tree.insert(0)
tree.insert(48)
tree.insert(12)
tree.insert(49)

class Solution(object):
    def __init__(self):
        self.prev_node = None
        self.min_diff = float('inf')

    def getMinimumDifference(self, root):
        self.inorder(root)
        return self.min_diff
    
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        if self.prev_node is not None:
            self.min_diff = min(self.min_diff, abs(node.value - self.prev_node.value))
        self.prev_node = node
        
print(Solution().getMinimumDifference(tree))
