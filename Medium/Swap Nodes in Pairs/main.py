# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):      
        dummy = ListNode(0, head)
        prev, curr_node = dummy, head 
        while curr_node and curr_node.next:
            # save ptrs
            nxt_pair = curr_node.next.next
            second_node = curr_node.next
            # reverse pairs
            second_node.next = curr_node
            curr_node.next = nxt_pair
            prev.next = second_node
            # update ptrs
            prev = curr_node
            curr_node = nxt_pair
        return dummy.next