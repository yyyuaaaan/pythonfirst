"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

Solution: 1. Iterative way (stack).   Time: O(n), Space: O(n).
           2. Recursive solution.      Time: O(n), Space: O(n).
           3. Threaded tree (Morris).  Time: O(n), Space: O(1).
vector<int> inorderTraversal_2(TreeNode *root) {
        vector<int> res;
        inorderTraversalRe(root, res);
        return res;
    }

    void inorderTraversalRe(TreeNode *node, vector<int> &res) {
        if (!node) return;
        inorderTraversalRe(node->left, res);
        res.push_back(node->val);
        inorderTraversalRe(node->right, res);
    }

"""