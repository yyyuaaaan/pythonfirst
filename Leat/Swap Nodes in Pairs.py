"""
Given a linked list, swap every two adjacent nodes and return its head.
 For example,
 Given 1->2->3->4, you should return the list as 2->1->4->3.
 Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

 Solution: 1. Iterative solution with constant space.
           2. Recursive solution with O(n) space (for practice).

 ListNode *swapPairs_1(ListNode *head) {
        ListNode dummy(0), *cur = &dummy;
        cur->next = head;
        while (cur->next && cur->next->next)
        {
            ListNode *move = cur->next->next;
            cur->next->next = move->next;
            move->next = cur->next;
            cur->next = move;
            cur = move->next;
        }
        return dummy.next;
    }

"""

def swapInPairs(head):
    if not head or not head.next: return head

    dummy =Node()
    dummy.next =head
    cur = dummy
    suc = head
    while cur is dummy or cur and suc:
        prev = cur
        cur=cur.next
        suc = suc.next
        prev.next = suc
        cur.next = suc.next
        suc.next = cur
    return dummy.next