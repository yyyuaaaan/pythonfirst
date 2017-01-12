"""__author__ = 'anyu'
First Common Ancestor
Design an algorithm and write code to find the first common ancestor of
 two nodes in a binary tree. Avoid storing additional nodes in a data structure.
 NOTE: This is not necessarily a binary search tree.

 If this were a binary search tree,we could modify the find operation for the two nodes
 and see where the paths diverge.

"""

class Node(object):
    def __init__(self):
        self.data= None
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return str(self.data)


def commonancester(tree,n1,n2):
    """
    # if with parent pointer, use hashtable and find intersect, same as intersect of two linked list
    # or go up one node, find the first node that cover another node, that's the lease common ancester
    if do not allow hashtable, then try one by one n1's parent, and test whether also n2's parent
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

def leastCommonAncesterBst(t, n1, n2):
    """
    bst no parent
    n1 !=n2.data
    input t must already be common ancenster, since n1, n2 is in the tree t
    bst no repetition
    """
    if n1.data< t.data and t.data<n2.data: # on both subtrees or root is one of them
        return t
    elif n2.data< t.data and t.data<n1.data: # on both subtrees or root is one of them
        return t
    elif n1.data== t.data or t.data==n2.data:
        return t
    elif n1.data<t.data and n2.data<t.data:
        leastCommonAncesterBst(t.left, n1, n2)
    elif t.data <n2.data and t.data < n1.data:
        leastCommonAncesterBst(t.right, n1, n2)

def findOneInNONBst(t,n):
    if not t:
        return None
    elif t.data==n.data:
        return True
    else:
        findOneInNONBst(t.left,n)
        findOneInNONBst(t.right,n)

def leastCommonAncesterNONBst(t, n1, n2):
    """
    #O(n) time, since each time findOneInNONBst halves
    This algorithm runs in O(n)time on a balanced tree.
    Alternatively, you could follow a chain in which p and q are on the same side.
    That is, if p and q are both on the left of the node, branch left to look for the common
    ancestor. If they are both on the right, branch right to look for the common ancestor.
    When p and q are no longer on the same side, you must have found the first common ancestor.

    """
    if t.data == n1.data or t.data == n2.data:
        return t
    elif findOneInNONBst(t.left, n1) and findOneInNONBst(t.right, n2) \
            or findOneInNONBst(t.left, n2) and findOneInNONBst(t.right, n1):
        return t
    else:
        leastCommonAncesterNONBst(t.right, n1, n2)
        leastCommonAncesterNONBst(t.left, n1, n2)

