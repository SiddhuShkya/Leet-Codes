class Solution(object):
    def middleNode(self, head):
        ln = self.getLen(head)
        cur_node = head
        mid = ln//2
        i = 0
        while i != mid:
            cur_node = cur_node.next
            i = i + 1
        return cur_node
    
    def getLen(self, head):
        cur_node = head
        ln = 0
        while cur_node:
            ln = ln + 1
            cur_node = cur_node.next
        return ln
