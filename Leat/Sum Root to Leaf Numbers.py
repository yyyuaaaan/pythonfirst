"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.


 Solution: 1. Recursion (add to sum when reaching the leaf).
           2. Iterative solution.


    int sumNumbers_1(TreeNode *root) {
        int sum = 0;
        sumNumbersRe(root, 0, sum);
        return sum;
    }

    void sumNumbersRe(TreeNode *node, int num, int &sum) {
        if (!node) return;
        num = num * 10 + node->val;
        if (!node->left && !node->right) {
            sum += num;
            return;
        }
        sumNumbersRe(node->left, num, sum);
        sumNumbersRe(node->right, num, sum);
    }
"""
def sumnum(root):

    def sumnumre(root,num,sum):
        if root is None: return
        num = num*10 + node.val
        if node.left is None and node.right is None:
            sum[0] += num
            return
        sumnumre(root.left,num,sum)
        sumnumre(root.right,num,sum)

    sum = [0]
    sumnumre(root,0,sum[0])
    return sum[0]
