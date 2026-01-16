def rotateRight(head, k):
    if not head:
        return head
    ln, tail = 1, head
    while tail.next:
        tail = tail.next
        ln += 1
    k = k%ln
    if k == 0:
        return head
    cur_node = head
    for i in range(ln - k -1):
        cur_node = cur_node.next
    new_head = cur_node.next
    cur_node.next = None
    tail.next = head
    return new_head
    