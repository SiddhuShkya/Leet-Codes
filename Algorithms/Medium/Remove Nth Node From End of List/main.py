class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, value):
        new_node = ListNode(value) 
        if self.next is None:  
            self.next = new_node
        else:
            current = self.next
            while current.next is not None:  
                current = current.next
            current.next = new_node



class Solution(object):

    def getSize(self, head):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count
        
    def removeNthFromEnd(self, head, n):
        size = self.getSize(head)
        idx = size - n
        i = 0
        prev_node = None
        current_node = head
        while i < idx:
            prev_node = current_node
            current_node = current_node.next
            i += 1
        if prev_node is None:
            head = head.next
        else:
            prev_node.next = current_node.next

        return head


linked_list = ListNode(1)

linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

print(Solution().removeNthFromEnd(linked_list, 1))


