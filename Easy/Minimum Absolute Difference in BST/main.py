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
                self.min_diff = min(self.min_diff, abs(node.val - self.prev_node.val))
            self.prev_node = node
            self.inorder(node.right)
