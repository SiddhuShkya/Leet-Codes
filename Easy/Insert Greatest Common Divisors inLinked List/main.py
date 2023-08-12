# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        cur_node = head
        while cur_node and cur_node.next:
            temp = cur_node.next
            gcd = self.greatestCommonDivisor(cur_node.val, cur_node.next.val)
            new_node = ListNode(gcd)
            cur_node.next = new_node
            new_node.next = temp
            cur_node = new_node.next
        return head
    
    def greatestCommonDivisor(self, m, n):
        if n == 0:
            return m
        return self.greatestCommonDivisor(n, m%n)