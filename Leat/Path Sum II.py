"""__author__ = 'anyu'
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

 For example:
 Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
 return
 [
   [5,4,11,2],
   [5,8,4,5]
 ]

 Solution: DFS.
 */

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 // O(n*h) time, O(h) space, h is the height of the tree
class Solution {
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<int> path;
        vector<vector<int> > res;
        pathSumHelper(root, sum, path, res);
        return res;
    }

    void pathSumHelper(TreeNode * cur, int sum, vector<int> & path, vector<vector<int> > & res) {
        if (cur == NULL) return;
        sum -= cur->val;
        path.push_back(cur->val);
        if (cur->left == NULL && cur->right == NULL && sum == 0) res.push_back(path);
        pathSumHelper(cur->left, sum, path, res);
        pathSumHelper(cur->right, sum, path, res);
        path.pop_back();
    }
};

class Solution {
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<vector<int>> res;
        vector<int> path;
        pathSumRe(root, sum, res, path);
        return res;
    }
    void pathSumRe(TreeNode *root, int sum, vector<vector<int>> &res, vector<int> &path)
    {
        if (!root) return;
        if (!root->left && !root->right)
        {
            if (sum == root->val)
            {
                path.push_back(root->val);
                res.push_back(path);
                path.pop_back();
            }
            return;
        }
        path.push_back(root->val);
        pathSumRe(root->left, sum - root->val, res, path);
        pathSumRe(root->right, sum - root->val, res, path);
        path.pop_back();
    }
};
"""
def pathSum(root, total):

    def pathSumHelper(root, total):
        if root.leftChild == None and root.rightChild == None:
            if total == root.data:
                path.append(root.data)
                results.append(list(path))
                path.pop()
            return
        path.append(root.data)
        if root.leftChild != None:
            pathSumHelper(root.leftChild, total - root.data)
        if root.rightChild != None:
            pathSumHelper(root.rightChild, total - root.data)
        path.pop()

    results = []
    path = []
    pathSumHelper(root, total)
    print(results)