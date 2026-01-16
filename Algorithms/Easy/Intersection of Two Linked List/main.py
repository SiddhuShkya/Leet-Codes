def getIntersectionNode(headA, headB):
    l1, l2 = 0, 0
    ha = headA
    hb = headB
    while ha:
        l1 += 1
        ha = ha.next
    while hb:
        l2 += 1
        hb = hb.next
    
    if l1 > l2:
        diff = l1 - l2
        while diff:
            headA = headA.next
            diff -= 1
    else:
        diff = l2 - l1
        while diff:
            headB = headB.next
            diff -= 1
    
    while headA and headB:
        headA = headA.next
        headB = headB.next
        if headA == headB:
            return headA
    return None
        
