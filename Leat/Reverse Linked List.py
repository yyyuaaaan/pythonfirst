"""__author__ = 'anyu'
public:
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        ListNode dummy(0), *ins = &dummy;
        dummy.next = head;
        for (int i = 0; i < m-1; ++i)
            ins = ins->next;
        ListNode *cur = ins->next;
        for (int i = 0; i < n-m; ++i) {
            ListNode *move = cur->next;
            cur->next = move->next;
            move->next = ins->next;
            ins->next = move;
        }
        return dummy.next;
    }

recursion will be concise? but too low efficient
"""
class ListNode:
    data = next = None

    def __init__(self, data):
        self.data = data

def generateLinkedList(array):
    if len(array) == 0:
        return None
    head = ListNode(array[0])
    curr = head
    for i in range(1, len(array)):
        node = ListNode(array[i])
        curr.next = node
        curr = node
    return head

def reverse(l):
    """
    recursion O(n2)
    """

    if not l or not l.next:
        return l

    first = l
    head = reverse(l.next)

    t = head
    tail = t
    while t:
        tail = tail.next

    tail.next = first
    first.next =None

    return head




