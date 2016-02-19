"""__author__ = 'anyu'
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
// Complexity:
// O(n) time
//============================================================================

#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *partition(ListNode *head, int x) {
        ListNode* frontHead = new ListNode(-1), *frontNode = frontHead;
        ListNode* backHead = new ListNode(-1), *backNode = backHead;
        while (head != NULL) {
            if (head->val < x) frontNode->next = head, frontNode = frontNode->next;
            else backNode->next = head, backNode = backNode->next;
            head = head->next;
        }
        backNode->next = NULL;
        frontNode->next = deleteNode(backHead);
        return deleteNode(frontHead);
    }

    ListNode * deleteNode(ListNode * curNode) {
        ListNode * toDel = curNode;
        curNode = curNode->next;
        delete toDel;
        return curNode;
    }
};
"""
def partition(L,val):
    if L is None: return L

    dummy = Node()
    dummy.next=L

    lt =Node()
    ltp=lt

    gr =Node()
    grp=gr

    while dummy.next:
        if dummy.next.val< val:
            ltp.next = dummy.next
        elif dummy.next.val>= val:
            grp.next = dummy.next
        dummy = dummy.next

    ltp.next = gr.next
    return lt.next