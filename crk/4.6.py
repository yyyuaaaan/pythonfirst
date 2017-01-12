"""__author__ = 'anyu'
Successor
Write an algorithm to find the next node ( in-order successor) of a given
node in a binary search tree where each node has a link to its parent.

assume there is a parent link to every node, but don't need it
This is not complex problem very tricky to code perfectly.
sketch out pseudocode to carefully outline the different cases.
 brute force   inorder  traversal then next

"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.neighbours=[]
    def __str__(self):
        return str(self.data)

def sucessor(root, node):
    #
    # very very tricky!
    # orders: 1, inner nodes, there is a right node, then the root is already considered!
    #         2, leaf node. pay attention to last element which has no successor
    #         3, remember left subtree is always smaller than right subtree
    #         4, draw a upstraght line of the node to be considered
    if not root:
        return None
    elif node.right:
        p= node.right
        while p.left:
            p=p.left
        return p

    else:
        # parents; search from root, don't use parent

        suc=None # root can >node or <node, if not, suc always none, or last node,
        temp=root

        #search and keep suc, suc just immediately > node
        while temp.data != node.data:
            if temp.data>node.data:
                suc=temp
                temp=temp.left
            else:
                temp=temp.right
        return suc

