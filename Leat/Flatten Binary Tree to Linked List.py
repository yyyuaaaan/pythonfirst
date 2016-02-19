"""__author__ = 'anyu'
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

 Hints:
 If you notice carefully in the flattened tree, each node's right child points to the next node
 of a pre-order traversal.

 Solution: Recursion. Return the last element of the flattened sub-tree.

class Solution {
public:
    void flatten(TreeNode *root) {
        TreeNode *end = NULL;
        flattenRe(root, end);
    }

    void flattenRe(TreeNode *node, TreeNode *&end) {
        if (!node) return;
        TreeNode *lend = NULL, *rend = NULL;
        flattenRe(node->left, lend);
        flattenRe(node->right, rend);
        if (node->left) {
            lend->right = node->right;
            node->right = node->left;
            node->left = NULL;
        }
        end = rend ? rend : (lend ? lend : node);
    }
};

class Solution {
public:
    void flatten(TreeNode *root) {
        while (root != NULL) {
            if (root->left != NULL) {
                TreeNode * rt = root->right;
                root->right = root->left;
                root->left = NULL;
                TreeNode * cur = root;
                while (cur->right) cur = cur->right;
                cur->right = rt;
            }
            root = root->right;
        }
    }
};
"""
