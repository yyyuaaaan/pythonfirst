"""__author__ = 'anyu'
4.5
Validate BST: Implement a function to check if a binary tree is a binary search tree.

sol1: inorder traversal into an array: extra space, and not work for dups
cannot distinguish between the two trees below (one of which is invalid) since they have the same in-order traversal.

My Approach1: Perform an inroder traversal and store the elements in O(n) time. Now scan through
the array/list of elements and check if element at ith index is greater than element at (i+1)th index.
If such a condition is encountered, return false and break out of the loop. (This takes O(n) time).
At the end return true.

bst must not have duplicates
if there is dupe cannot use an  extra array to do inorder traversal
"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

def is_bst(tree):
    """
    dfs O(n)  space and O(n) time; with dups is ok; wrong!!! need to check tree<tree.left.smallest, its successor
    """
    if not tree or not tree.left and not tree.right:
        return True
    elif tree.right and tree.data> tree.right.data: # check tree.data>tree.right.right......rightn no! all subtree
                                                            #has to be checked
            return False
    elif tree.left and tree.data<= tree.left.data:
            return False
    else:
        return is_bst(tree.right) and is_bst(tree.left)

def bstcheckinorder(tree, prev=None):
    """
    in order traversal, need to keep prev value, out of  the function O(N)
    implicit o(n) space, so array is prefered, bst must use inorder traversal

    """
    if not tree:
        return True
    else:
        if not bstcheckinorder(tree.left, prev):
            return False

        if prev and prev>=tree.data: # = is ok, then prev>tree.data
            return False
        else:
            prev = tree.data

        if not bstcheckinorder(tree.right, prev):
            return False
        return True

def isbstminmax(tree, min = -1000, max=1000):
    """
    in order traversal, keep track of min and max
    :param tree:
    :return:
    o(n) time and logn space
    """
    if not tree:
        return True
    else:
        return min<tree.data and tree.data<max and\
               isbstminmax(tree.left, min, tree.data) and isbstminmax(tree.right, tree.data, max)
