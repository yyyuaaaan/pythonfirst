"""__author__ = 'anyu'
Sort a linked list using insertion sort.
ListNode *insertionSortList(ListNode *head) {
        ListNode dummy(INT_MIN);
        dummy.next = head;
        ListNode *cur = &dummy;
        while (cur->next) {
            if (cur->next->val >= cur->val)
                cur = cur->next;
            else
                insert(&dummy, cur, cur->next);
        }
        return dummy.next;
    }

    void insert(ListNode *head, ListNode *tail, ListNode *node) {
        ListNode *cur = head;
        while (cur->next->val < node->val)
            cur = cur->next;
        tail->next = node->next;
        node->next = cur->next;
        cur->next = node;
    }

"""
def insertionsortlist(head):
    dummy = Node()
    dummy.next = head
    cur = dummy
    while cur.next:
        if cur.next.val >= cur.val:
            cur = cur.next
        else:
            insert(dummy,cur,cur.next)
    return dummy.next

def insert(head,tail,node):
    cur = head
    while cur.next.val < node.val:
        cur = cur.next
    cur.next=node

    tail.next = node.next
    node.next=cur.next
