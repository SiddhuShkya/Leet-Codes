class Solution(object):
    def hasCycle(self, head):
        seen = set()
        while head:
            if head in seen: 
                return True
            seen.add(head)
            head = head.next
        return False