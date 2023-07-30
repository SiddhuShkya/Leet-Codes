def deleteDuplicates(head):
    cur_node = head
    prev_node = None
    while cur_node and cur_node.next:
        next_node = cur_node.next
        if cur_node.val == next_node.val:
            while next_node and cur_node.val == next_node.val:
                next_node = next_node.next 
            if prev_node:
                prev_node.next = next_node
            else:
                head = next_node          
            cur_node = next_node
        else:
            prev_node = cur_node
            cur_node = next_node
    return head