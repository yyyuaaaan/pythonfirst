"""
 Given a linked list, determine if it has a cycle in it.
 Solution: two pointers.

 do not allow extra space, but i love hashtable!

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head || !head->next) return false;
        ListNode *slow = head, *fast = head->next->next;
        while (true)
        {
            if (fast == slow) return true;
            if (!fast || !fast->next) return false;
            fast = fast->next->next;
            slow = slow->next;
        }
    }
};
"""
def loop(l):
    if not l or not l.next: return None
    else:
        s=set()
        dummy = Node()
        dummy.next = l
        while dummy.next:
            if hash(dummy.next) in s:
                return dummy.next
            else:
                s.add(hash(dummy.next))
