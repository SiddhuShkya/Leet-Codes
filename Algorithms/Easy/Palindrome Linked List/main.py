class Solution(object):
    def isPalindrome(self, head):
        res = ""
        while head:
            res += str(head.val)
            head = head.next
        if res == res[::-1]:
            return True
        return False