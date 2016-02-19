"""__author__ = 'anyu'
4.5 Implemen t a function to check if a binary tree is a binary search tree.
Our first thought might be to do an in-order traversal, copy the elements to an array,
and then check to see if the array is sorted.This solution takes up a bit of extra memory, but it works mostly.
just say it takes more space

The only problem is that it can't handle duplicate values in the tree properly. For
example, the algorithm cannot distinguish between the two trees below (one of which
is invalid)since they have the same in-order traversal.
However, if we assume that the tree cannot have duplicate values,then this approach works

My Approach1: Perform an inroder traversal and store the elements in O(n) time. Now scan through
the array/list of elements and check if element at ith index is greater than element at (i+1)th index.
If such a condition is encountered, return false and break out of the loop. (This takes O(n) time).
At the end return true.


bst must not have duplicates
"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)


def is_bst(tree): # this is wrong!!! check subtree, not just left right node
    """
    dfs O(n)
    :param tree:
    :return:

    """
    if not tree or not tree.left and not tree.right:
        return True
    else:
        if tree.right and tree.data>= tree.right.data:
            return False
        if tree.left and tree.data<= tree.left.data:
            return False
        return is_bst(tree.right) and is_bst(tree.left)



def bstcheckinorder(tree, prev=None):
    """
    in order traversal, need to keep prev value, out of  the function O(N)
    :param tree:
    :return:
    """

    if not tree:
        return True
    else:

        bstcheckinorder(tree.left, prev)

        if prev is not None and prev>=tree.data:
            return False
        prev = tree.data

        bstcheckinorder(tree.right, prev)

        return True


def isbstminmax(tree, min = -1000, max=1000):
    """
    in order traversal, keep track of min and max
    :param tree:
    :return:
    """
    if not tree:
        return True
    elif tree.data <=min or tree.data>=max: # need to be unique , no dup
        return False
    else:
        return isbstminmax(tree.left, min, tree.data) and isbstminmax(tree.right, tree.data, max)