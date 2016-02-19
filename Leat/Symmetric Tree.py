"""

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

 Solution: 1. Recursive solution 2.Iterative way (queue).

    bool isSymmetric_1(TreeNode *root) {
        if (!root) return true;
        return isSymmetricRe(root->left, root->right);
    }

    bool isSymmetricRe(TreeNode *t1, TreeNode *t2)
    {
        if (!t1 && !t2) return true;
        if (!t1 || !t2 || t1->val != t2->val) return false;
        return isSymmetricRe(t1->left, t2->right) &&
               isSymmetricRe(t1->right, t2->left);
    }
"""
def isSymmetric_1(root):
    if not root: return True
    return isSymmetricRe(root.left, root.right)

def isSymmetricRe(t1,t2):
    if not t1 and not t2: return True
    if (not t1 or not t2) or t1.val != t2.val: return False
    return isSymmetricRe(t1.left, t2.right) and isSymmetricRe(t1.right, t2.left)