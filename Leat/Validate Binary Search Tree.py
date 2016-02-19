"""__author__ = 'anyu'
Validate Binary Search Tree Total Accepted: 8305 Total Submissions: 32869 My Submissions
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
Solution: Recursion. 1. Add lower & upper bound. O(n)
                      2. Inorder traversal with one additional parameter (value of predecessor). O(n)
class Solution {
public:
    bool isValidBST(TreeNode *root) {
        return isValidBST_1(root);
    }

    // solution 1: lower bound + higher bound
    bool isValidBST_1(TreeNode *root) {
        return isValidBSTRe_1(root, INT_MIN, INT_MAX);
    }

    bool isValidBSTRe_1(TreeNode *node, int lower, int upper){
        if (!node) return true;
        if (node->val <= lower || node->val >= upper) return false;

        return isValidBSTRe_1(node->left, lower, node->val) &&
               isValidBSTRe_1(node->right, node->val, upper);
    }

    // solution 2: inorder
    bool isValidBST_2(TreeNode *root) {
        int val = INT_MIN;
        return isValidBSTRe_2(root, val);
    }

    bool isValidBSTRe_2(TreeNode *node, int &val)
    {
        if (!node) return true;
        if (node->left && !isValidBSTRe_2(node->left, val))
            return false;
        if (node->val <= val)
            return false;
        val = node->val;
        if (node->right && !isValidBSTRe_2(node->right, val))
            return false;
        return true;
    }
};


"""
def isValidBSTRe(root):
    """
    wrong
    """
    if not root or not root.left and not root.right: return True
    elif root.left and root.left.val>= root.val: return False
    elif root.right and root.right.val<=root.val: return False
    else:
        return isValidBSTRe(root.left) and isValidBSTRe(root.right)
"""
    // solution 1: lower bound + higher bound
    bool isValidBST_1(TreeNode *root) {
        return isValidBSTRe_1(root, INT_MIN, INT_MAX);
    }

    bool isValidBSTRe_1(TreeNode *node, int lower, int upper){
        if (!node) return true;
        if (node->val <= lower || node->val >= upper) return false;

        return isValidBSTRe_1(node->left, lower, node->val) &&
               isValidBSTRe_1(node->right, node->val, upper);
"""
def isvalidbst(root):
    def isValidBSTRe_1(root, lower,upper):
        if not root: return True
        if root.val<= lower or root.val>=upper: return False
        return isValidBSTRe_1(root.left, lower, root.val) and isValidBSTRe_1(root.right, root.val, upper)

    return isValidBSTRe_1(root, -100000, 10000000)