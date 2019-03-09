def addTwoNumbers(self, l1, l2):
    a = l1
    while l1.next and l2.next:
        l1.val = l1.val + l2.val
        if l1.val >= 10:
            l1.val = l1.val - 10
            l1.next.val = l1.next.val + 1
        l1, l2 = l1.next, l2.next
    if l1.next:
        l1.val = l1.val + l2.val
        if l1.val >= 10:
            l1.val = l1.val - 10
            l1.next.val = l1.next.val + 1
        while l1.next:
            l1 = l1.next
            if l1.val >= 10:
                l1.val = l1.val - 10
                if l1.next:
                    l1.next.val = l1.next.val + 1
                else:
                    break
            else:
                break
    elif l2.next:
        l2.val = l1.val + l2.val
        l1 = l2
        if l1.val >= 10:
            l1.val = l1.val - 10
            l1.next.val = l1.next.val + 1
        while l1.next:
            l1 = l1.next
            if l1.val >= 10:
                l1.val = l1.val - 10
                if l1.next:
                    l1.next.val = l1.next.val + 1
                else:
                    break
            else:
                break
    else:
        l1.val = l1.val + l2.val
    if l1.val >= 10:
        l1.val = l1.val - 10
        l1.next = ListNode(1)
    return a
