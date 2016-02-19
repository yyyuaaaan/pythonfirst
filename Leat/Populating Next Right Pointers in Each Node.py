"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

 Solution: 1. Iterative: Two 'while' loops: root->leaf and left->right.
           2. Iterative: Queue. Use extra space.
           3. Recursive: DFS. Defect: Use extra stack space for recursion.
    void connect_3(TreeLinkNode *node) {
        if (!node || !node->left) return;
        node->left->next = node->right;
        node->right->next = node->next ? node->next->left : NULL;
        connect_3(node->left);
        connect_3(node->right);

"""