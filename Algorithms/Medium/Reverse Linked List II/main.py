
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    subList = []
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    # Move prev to the node just before the left position
    for _ in range(left - 1):
        prev = prev.next
    cur = prev.next
    for _ in range(right - left + 1):
        subList.append(cur.val)
        cur = cur.next
    temp = cur
    sub_list_head = getReverseLList(subList)
    prev.next = sub_list_head
    while prev.next:
        prev = prev.next
    prev.next = temp
    return dummy.next

def getReverseLList(subList):
    new_head = ListNode(subList.pop())
    cur_node = new_head
    while subList:
        num_node = ListNode(subList.pop())
        cur_node.next = num_node
        cur_node = cur_node.next
    return new_head

         

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

print(reverseBetween(node1, 2, 4))


        