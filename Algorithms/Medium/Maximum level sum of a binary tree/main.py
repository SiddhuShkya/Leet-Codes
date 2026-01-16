class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val > self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)


tree = TreeNode(1)
tree.insert(0)
tree.insert(7)
tree.insert(7)
tree.insert(-8)


class Solution(object):
    def __init__(self):
        self.hp = {}
        self.level = 0

    def maxLevelSum(self, root):
        if root is None:
            return 0

        self.dfs(root, 1)
        max_sum = float('-inf')
        max_level = 1
        for level, level_sum in self.hp.items():
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

        return max_level

    def dfs(self, node, level):
        if level not in self.hp:
            self.hp[level] = 0

        self.hp[level] += node.val

        if node.left:
            self.dfs(node.left, level + 1)

        if node.right:
            self.dfs(node.right, level + 1)


print(Solution().maxLevelSum(tree))
