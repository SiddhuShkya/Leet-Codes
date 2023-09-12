# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head:
        return head

    # Helper function to merge two sorted lists.
    def merge(left, right):
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        if left:
            current.next = left
        if right:
            current.next = right

        return dummy.next

    # Split the list into two halves.
    def split(head):
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        return head, slow

    # Merge sort the two halves.
    def merge_sort(head):
        if not head or not head.next:
            return head
        left, right = split(head)
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

    return merge_sort(head)

node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4

sorted_head = sortList(node1)

# Print the sorted values of the linked list.
current = sorted_head
while current:
    print(current.val, end=" ")
    current = current.next
