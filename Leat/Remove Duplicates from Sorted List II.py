"""__author__ = 'anyu'
Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

 Solution: 1. Delete duplicates directly.

"""
def deleteDuplicates(l):
    if l is None or l.next is None:return l
    cur =l

    while cur.next is not None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        cur = cur.next
    return l
