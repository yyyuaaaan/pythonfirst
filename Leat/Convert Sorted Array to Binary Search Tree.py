"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

recursion
    TreeNode *sortedArrayToBST(vector<int> &num) {
        return buildBST(num, 0, num.size() - 1);
    }

    TreeNode *buildBST(vector<int> &num, int start, int end)
    {
        if (start > end) return NULL;

        int mid = (start + end) / 2;
        TreeNode *root = new TreeNode(num[mid]);
        root->left = buildBST(num, start, mid - 1);
        root->right = buildBST(num, mid + 1, end);

        return root;
    }
"""
def sortedArrayToBST(numlist):
    return buildBST(numlist,0,len(numlist)-1)

def buildBST(num, start, end):
    if start>end: return None
    mid = (start+end)/2

    root = Node(num[mid])
    root.left = buildBST(num, start, mid-1)
    root.right = buildBST(num, mid+1, end)
    return root