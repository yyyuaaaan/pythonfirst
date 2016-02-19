"""__author__ = 'anyu'
h
Design an algorithm and write code to find the first common ancestor of
 two nodes in a binary tree. Avoid storing additional nodes in a data structure.
 NOTE: This is not necessarily a binary search tree.

 If this were a binary search tree,we could modify the find operation for the two nodes
 and see where the paths diverge. Unfortunately, this is not a binary search tree, so we must
 try other approaches.

 1,hashtable
 2,iteratively do n1's parent, until find the common, or root
 3,post order traversal!!! and push into stack! topological sort, (1)one stack, still have to do every node
                                                                  (2)two stack from n1 and n2, when you pop out the first common node!
                                                                  bingo! complex!
 4,if no parent pointer: from root, do recursion.


"""

class Node(object):
    def __init__(self):
        self.data= None
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return str(self.data)


def commonAncestor3_helper(n1, n2, tree): # no parent pointer, hard! and complex!
    """Alternatively, you could follow a chain in which p and q are on the same side.
    That is, if p and q are both on the left of the node, branch left to look for the common
    ancestor. If they are both on the right, branch right to look for the common ancestor.
    When p and q are no longer on the same side, you must have found the first common ancestor.

    This algorithm runs in O(n)time on a balanced tree.
    """
    # when do this recursion, we keep track fo two things, isancester? and node to return, a smart technique!
    # no! [True, tree] is not smart ,it is stupid, making things complex

    if tree is None: return None
    if tree is n1 or tree is n2: return tree  # this line can be omited, need to double check
    if isancestor(n1,tree.left) and isancestor(n2, tree.right)\
        or isancestor(n1, tree.right) and isancestor(n2, tree.left):
        return tree

    if isancestor(n1,tree.left) and isancestor(n2, tree.left:
        return commonAncestor3_helper(n1, n2, tree.left)
    else:
        return commonAncestor3_helper(n1, n2, tree.right)

def find(tree, n1,n2):
    """
    if it is bst, then following is ok
    :param tree:
    :param n1:
    :param n2:
    :return:
    """
    if not tree:
        return
    elif tree.data<n2.data and tree.data>n1.data:
        return tree
    elif tree.data>n2.data and tree.data>n1.data:
        return find(tree.right,n1,n2)
    else:
        return find(tree.left,n1,n2)


def commonancester(tree,n1,n2):
    """
    if has a parent pointer: then use hashtable
    if do not allow hashtable, then try one by one n1's parent, and test whether also n2's parent
    :param tree:
    :param n1:
    :param n2:
    :return:
    """
    if not tree:
        return
    elif not n1 and not n2:
        return
    elif not n1:
        if n2.parent:
            return n2.parent
        else:
            return
    elif not n2:
        if n1.parent:
            return n1.parent
        else:
            return
    else:
        hashn1=[]
        while n1.parent:
            if n1.parent not in hashn1:
                hashn1.append(n1.parent)
        p= n2.parent
        while p:
            if p not in hashn1:
                p=p.parent
            elif p in hashn1:
                return p
            else:
                return

def commances(tree,n1,n2):
    """
    no parent pointer and no ancestor
    then have to test from the root one by one
    O(logn) san ci fang?
    :param n1:
    :param n2:
    :return:
    """

    def father(ancestor,child):
        if not ancestor:
            return False
        elif ancestor == child:
            return True
        else:
            father(ancestor.right, child) or father(ancestor.left, child)
    if not tree:
        return
    elif not father(tree,n1) or father(tree,n2):

        # tree must be the ancestor of n1 and n2
        return
    else:
        p = tree
        while father(p, n1) and father(p, n2):
            if father(tree.left, n1) and father(tree.left, n2):
                p = tree.left
            elif father(tree.right, n1) and father(tree.right, n2):
                p = tree.right
            else:
                return p



