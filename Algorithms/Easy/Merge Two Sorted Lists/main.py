class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.insert(val)
    
    def display(self):
        elems = []
        cur_node = self
        while cur_node is not None:
            elems.append(cur_node.val)
            cur_node = cur_node.next
        return elems

l1 = ListNode(1)
l1.insert(3)
l1.insert(5)
l1.insert(7)
l2 = ListNode(1)
l2.insert(2)
l2.insert(3)
l2.insert(6)
print(l1.display())
print(l2.display())

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2
        return dummy.next
    
    def display(self, head):
        elems = []
        cur_node = head
        while cur_node is not None:
            elems.append(cur_node.val)
            cur_node = cur_node.next
        return elems

s = Solution()
mergedList = s.mergeTwoLists(l1, l2)
print(s.display(mergedList))



