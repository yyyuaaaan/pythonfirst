"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?


 Solution: 1. Iterative way (stack).   Time: O(n), Space: O(n).
           2. Recursive solution.      Time: O(n), Space: O(n).

  vector<int> postorderTraversal_1(TreeNode *root) {
        vector<int> res;
        stack<TreeNode *> stk;
        TreeNode *last = NULL, *cur = root;
        while(cur || !stk.empty()){
            if (cur) {
                stk.push(cur);
                cur = cur->left;
            }
            else{
                TreeNode *peak = stk.top();
                if(peak->right && last != peak->right)
                    cur = peak->right;
                else{
                    res.push_back(peak->val);
                    stk.pop();
                    last = peak;
                }
            }
        }
        return res;
    }

    vector<int> postorderTraversal_2(TreeNode *root) {
        vector<int> res;
        postorderTraversalRe(root, res);
        return res;
    }

    void postorderTraversalRe(TreeNode *node, vector<int> &res) {
        if (!node) return;
        postorderTraversalRe(node->left, res);
        postorderTraversalRe(node->right, res);
        res.push_back(node->val);
"""

def postorderTraversal_1(root):
    res = []
    stack = []
    last=None
    cur = root
    while cur is not None or stack is not []:
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            peak = stack[len(stack)-1]
            if peak.right and last != peak.right:
                cur = peak.right
            else:
                res.append(peak.val)
                stack.pop()
                last = peak





def postorderTraversal_2(root):
    def postorderTraversalRe(root, res):
        if not root: return
        postorderTraversal_2(root.left, res)
        postorderTraversal_2(root.right, res)
        res.append(root.val)
    res =[]
    postorderTraversalRe(root,res)
    return res
