class Solution(object):
    def getDecimalValue(self, head):
        res = 0
        strRes = ""
        while head:
            strRes += str(head.val) 
            head = head.next
        c = 1
        for i in range(len(strRes) - 1, -1, -1):
            if strRes[i] == "1":
                res += c
            c = c * 2
        return res