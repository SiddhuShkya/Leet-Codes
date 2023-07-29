
def removeElements(self, head, val):
    while head and head.val == val:
        head = head.next
    cur_node = head
    while cur_node and cur_node.next:
        if cur_node.next.val == val:
            cur_node.next = cur_node.next.next
        else:
            cur_node = cur_node.next
    return head