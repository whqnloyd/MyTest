def addTwoNumbers(self, l1, l2):
    s = 0
    l3 = []
    while l1.next and l2.next:
        l3.append((l1.val + l2.val + s) % 10)
        s = int((l1.val + l2.val + s) / 10)
        l2, l1 = l1.next, l2.next

    l3.append((l1.val + l2.val + s) % 10)
    s = int((l1.val + l2.val + s) / 10)

    if l1.next:
        l1 = l1.next
        while l1.next:
            l3.append((l1.val + s) % 10)
            s = int((l1.val + s) / 10)
            l1 = l1.next
        l3.append((l1.val + s) % 10)
        s = int((l1.val + s) / 10)
    elif l2.next:
        l2 = l2.next
        while l2.next:
            l3.append((l2.val + s) % 10)
            s = int((l2.val + s) / 10)
            l2 = l2.next
        l3.append((l2.val + s) % 10)
        s = int((l2.val + s) / 10)

    if s != 0:
        l3.append(1)

    return l3
