# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        dummy_small = ListNode(0)  # dummy node for values smaller than x
        dummy_large = ListNode(0)  # dummy node for values greater than or equal to x
        small = dummy_small
        large = dummy_large

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None  # set the tail of the large list to None
        small.next = dummy_large.next  # connect the smaller list to the larger list
        return dummy_small.next



node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ll = Solution()
ll.partition(node1, 3)
