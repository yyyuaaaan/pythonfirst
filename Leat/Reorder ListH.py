"""__author__ = 'anyu'
hard, detail

Given a singly linked list L: L0-L1--L(n-1)-Ln,
reorder it to: L0-Ln-L1-L(n-1)-L2-L(n-2)-

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

 Solution: Reverse the back half first, then reorder.
 O(N) time complexity and O(1) space complexity

void reorderList2(ListNode *head) {
        if (head == NULL || head->next == NULL) return;
        ListNode * frontHead, *backHead;
        split(head, frontHead, backHead);
        backHead = reverse(backHead);
        merge(frontHead, backHead);
    }

    void split(ListNode * head, ListNode *& frontHead, ListNode *& backHead) {
        ListNode * fastNode = head, *slowNode = head;
        for (; fastNode->next != NULL && fastNode->next->next != NULL; fastNode = fastNode->next->next) slowNode = slowNode->next;
        backHead = slowNode->next;
        slowNode->next = NULL;
        frontHead = head;
    }

    ListNode * reverse(ListNode * head) {
        ListNode * preNode = NULL, *curNode = head;
        while (curNode) {
            ListNode * nextNode = curNode->next;
            curNode->next = preNode;
            preNode = curNode;
            curNode = nextNode;
        }
        return preNode;
    }

    void merge(ListNode * frontHead, ListNode * backHead) {
        ListNode * head = pushDummy(NULL), *curNode = head;
        while (frontHead || backHead) {
            if (frontHead) curNode->next = frontHead, frontHead = frontHead->next, curNode = curNode->next;
            if (backHead) curNode->next = backHead, backHead = backHead->next, curNode = curNode->next;
        }
        head = popDummy(head);
    }

    ListNode * pushDummy(ListNode * head) {
        ListNode * newNode = new ListNode(-1);
        newNode->next = head;
        return newNode;
    }

    ListNode * popDummy(ListNode * head) {
        ListNode * delNode = head;
        head = head->next;
        delete delNode;
        return head;
    }
};

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None: return
        slow = head
        fast = head.next.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        if fast is not None:
            slow = slow.next

        mid = slow
        cur = slow.next
        while cur.next is not None: # reverse
            mov = cur.next
            cur.next = mov.next
            mov.next = mid.next
            mid.next = mov

        cur = head
        while cur is not mid and mid.next is not None: # insert merge
            mov = mid.next
            mid.next = mov.next
            mov.next = cur.next
            cur.next = mov
            cur = cur.next.next
        return head
