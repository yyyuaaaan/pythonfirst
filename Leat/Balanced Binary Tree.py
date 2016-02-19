"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of t
he two subtrees of every node never differ by more than 1.

 bool isBalanced(TreeNode *root) {
        int height = 0;
        return isBalancedRe(root, height);
    }

    bool isBalancedRe(TreeNode *root, int &height){
        if (!root) return true;

        int leftHeight = 0, rightHeight = 0;
        if (!isBalancedRe(root->left, leftHeight)) return false;
        if (!isBalancedRe(root->right, rightHeight)) return false;
        if (abs(leftHeight-rightHeight) > 1) return false;

        height = 1 + max(leftHeight, rightHeight);
        return true;
    }
"""
def isBalanced(root):

    """
    this is not right, use another function to get depth of tree
    """

    def isBalancedRe(root, height):
        if not root or not root.left and root.right: return True,height

        rightbalanced,rh= isBalancedRe(root.right,height+1)
        leftbalanced,lh = isBalancedRe(root.left,height+1)
        if not rightbalanced or not leftbalanced: return False
        else:
            return abs(rh - lh) <=1

    return isBalancedRe(root,0)
