# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        
        # Function to compute height of a subtree
        def compute_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        left_height = compute_height(root.left)
        right_height = compute_height(root.right)
        
        if left_height == right_height:
            # Left subtree is a perfect binary tree
            return (2 ** left_height) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree
            return (2 ** right_height) + self.countNodes(root.left)
        