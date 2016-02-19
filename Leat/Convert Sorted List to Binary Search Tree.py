"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


 Solution: Recursion. Pre-order. O(n)
class Solution {
public:
    TreeNode *sortedListToBST(ListNode *head) {
        return sortedListToBSTRe(head, getLength(head));
    }

    TreeNode *sortedListToBSTRe(ListNode *&head, int length)
    {
        if (length == 0) return NULL;
        int mid = length / 2;
        TreeNode *left = sortedListToBSTRe(head, mid);
        TreeNode *root = new TreeNode(head->val);
        TreeNode *right = sortedListToBSTRe(head->next, length - mid - 1);
        root->left = left;
        root->right = right;
        head = head->next;
        return root;
    }

    int getLength(ListNode *head)
    {
        int length = 0;
        while (head)
        {
            length++;
            head = head->next;
        }
        return length;
    }
};
"""