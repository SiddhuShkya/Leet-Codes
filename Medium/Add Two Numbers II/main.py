class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def reverse_linked_list(self, head):
            stack = []
            while head:
                stack.append(head.val)
                head = head.next
            new_head = ListNode(stack.pop())
            current = new_head
            while stack:
                current.next = ListNode(stack.pop())
                current = current.next
            return new_head

    def addTwoNumbers(self, l1, l2):
        l1 = self.reverse_linked_list(l1)
        l2 = self.reverse_linked_list(l2)
        carry = 0
        result_head = None
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            remainder = total_sum % 10
            new_node = ListNode(remainder)
            if result_head is None:
                result_head = new_node
            else:
                new_node.next = result_head
                result_head = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result_head
