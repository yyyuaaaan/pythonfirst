"""__author__ = 'anyu'
Write an algorithm to find the ‘next’ node (i.e., in-order successor) of a given
node in a binary search tree where each node has a link to its parent.

This is not the most algorithmically complex problem in the world,
but it can be tricky to code perfectly. In a problem like this, it's useful to sketch
out pseudocode to carefully outline the different cases.


"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.neighbours=[]
    def __str__(self):
        return str(self.data)

def nextnodedfs(tree, llist=[]):
    """
    inorder dfs traversal
    """
    if tree is None:  #	or: if btree is None: return True .
        return llist

    if tree.left: nextnodedfs(tree.left)
    llist.append(tree)
    if tree.right: nextnodedfs(tree.right)

def nextnodeaddr(llist,node):
    return llist.index(node)+1


def nextnodedirectfetch(node):
    """
    very very tricky!
    orders: 1, inner nodes, there is a right node, then the root is already considered!
            2, leaf node. pay attention to last element which has no successor
            3, remember left subtree is always smaller than right subtree
            4, draw a upstraght line of the node to be considered
    """
    if not node: return
    elif node.right is not None:
        p = node.right
        while p.left is not None:
            p= p.left
        return p
    else:
        p=node
        while p.parent and p.parent.data <= p.data: # while node is p.right: wrong!!   just have to find the first parent that is bigger
            p = p.parent
        if not p:
            print "last element, no next"
            return
        else:
            return p
