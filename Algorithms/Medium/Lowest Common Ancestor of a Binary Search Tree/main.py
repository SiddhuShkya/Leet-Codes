from BST import BinaryTree

def lowestCommonAncestor(root, p, q):
    cur_node = root
    while cur_node:
        if (p.val > cur_node.val and q.val > cur_node.val):
            cur_node = cur_node.right
        elif (p.val < cur_node.val and q.val < cur_node.val):
            cur_node = cur_node.left
        else:
            return cur_node

tree = BinaryTree(6)
tree.insert(2)
tree.insert(8)
tree.insert(0)
tree.insert(4)
tree.insert(7)
tree.insert(3)
tree.insert(5)

p = BinaryTree(2)
q = BinaryTree(4)

print(lowestCommonAncestor(tree, p, q))



