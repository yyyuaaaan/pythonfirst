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
def height(tree):
    if tree.left==None and tree.right==None:
        return 0
    return max(height(tree.left),height(tree.right))+1

def isbalanced(tree):
    if tree.left==None and tree.right==None:
        return True
    else:
        return abs(height(tree.left)- height(tree.right)) <=1 and\
            isbalanced(tree.left) and isbalanced(tree.right)    # this must be checked
#On each node, we recurse through its entire subtree.
# This means that getHeight is called repeatedly on the same nodes.
# The algorithm is therefore O(N2).
#effcient algorithm, get heights of subtrees and check subtrees if balanced at the same time O(V+E)= O()

# similar to DFS, post-order traversal

def isbalanced3(tree, height=0):
    if not tree or not tree.left and not tree.right:
        return [True,height]
    else:
        [isleftbalanced, leftheight] = isbalanced(tree.left,height+1)
        [isrightbalanced, rightheight] = isbalanced(tree.right,height+1)
        return isleftbalanced and isrightbalanced and \
               abs(leftheight-rightheight)<=1


isbalanced3(tree,0)
