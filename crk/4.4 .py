"""__author__ = 'anyu'

Implement a function to check if a tree is balanced.
For the purposes of this question, a balanced tree is defined
to be a tree such that the heights of the two subtrees of any     # this is so called AVL-tree
node never differ by more than one.

"""

class Node(object):
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None

    def __str__(self):
        return "data:"+str(self.data)+"("+str(self.left)+"|"+str(self.right)+")"+"depth:"+str(self.depth)

#O(n^2) naive algorithm

def heightoftree(t):
    if not t:
        return 0
    else:
        return max(heightoftree(t.left)+1, heightoftree(t.right)+1)
def checkavl(t):
    if not t:
        return True
    elif abs(heightoftree(t.left)-heightoftree(t.right))<=1:
        return checkavl(t.left) and checkavl(t.right)
    else:
        return False

#On each node, we recurse through its entire subtree.
# This means that getHeight is called repeatedly on the same nodes.
# The algorithm is therefore O(N2).
#effcient algorithm, get heights of subtrees and check subtrees if balanced at the same time O(V+E)= O()

def heightandavl(t):
    """
    o(n) time and O(logn) space, space is the height
    """
    if not t:
        return 0
    else:
        h1= heightandavl(t.left)
        h2= heightandavl(t.right)

        if  abs(h1 - h2)>1 or h1<0 or h2<0: #must include h1<0 and h2<0
            return -1 # one num to denote False

        # wrong! return abs(h1-h2)<=1
        return max(h1, h2)+1 #if height>=0 then True
