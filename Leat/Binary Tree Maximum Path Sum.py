"""
Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.
For example:
Given the below binary tree,
       1
      / \
     2   3
Return 6.
public int maxPathSum(TreeNode root) {
    int[] res = new int[1];
    res[0] = Integer.MIN_VALUE;
    maxPath(root, res);
    return res[0];
}
private int maxPath(TreeNode root, int[] res) {
    if (root == null)
        return 0;
    int left = maxPath(root.left, res);//左边一支儿（不算自己）
    int right = maxPath(root.right, res);
    int arch = left + right + root.val; //穿过自己
    int single = Math.max(root.val, Math.max(left, right) + root.val);（算上自己）
    res[0] = Math.max(res[0], Math.max(arch, single));//update结果
    return single;
}

"""

def maxPathSum(root):

    def maxpath(root, res):
        if root is None:
            return 0
        left = maxpath(root.left,res)
        right = maxpath(root.right,res)
        arch = left + right + root.val
        single = max(root.val,max(left,right)+root.val)
        res[0] = max(res[0], max(arch,single))
        return single

    res =[-100000]
    maxpath(root,res)
    return res[0]

