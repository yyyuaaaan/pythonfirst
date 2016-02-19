"""
Merge two sorted linked lists and return it as a new list.
 The new list should be made by splicing together the nodes of the first two lists.



"""
def merge(L1, L2):
    dummy = Node()
    cur = dummy
    p1 = L1
    p2 = L2
    while p1 and p2:
        if p1.val < p2.val:
            cur.next =p1
            cur = cur.next
            p1 = p1.next
        else:
            cur.next = p2
            cur = cur.next
            p2 = p2.next
    if p1: cur.next = p1
    if p2: cur.next = p2
    return dummy.next


