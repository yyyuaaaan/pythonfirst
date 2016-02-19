"""__author__ = 'anyu'

kan kan jiu xing, messy
only in the 5th edition

17.13 Consider a simple node-like data structure called BiNode,which has pointers to two other nodes. The data structure BiNode
could be used to represent both a binary tree (where node1 is the left node and node2 is the right node) or a
doubly linked list (where node l is the previous node and node2 is the next node). Implement a method to convert a
binary search tree (implemented with BiNode) into a doubly linked list. The values should be kept in order and the
operation should be performed in place (that is,on the original data structure).

Solution

This seemingly complex problem can be implemented quite elegantly using recursion. You will need to understand
recursion very well to solve it.
 So, if we recursively converted the left and right subtrees to a doubly linked list,  we could build the final
 linked list from those parts
The pseudocode looks something like:
1 BiNode convert(BiNode node) {
2  BiNode left = convert(node.left);
3  BiNode right = convert(node.right);
4  mergeLists(left, node, night);
5  return left; // front of left
6}
we'll need to get the head and tail of each linked list. We can do this several different ways.

why can't we use inorder traversal?????, this stupid space saving only make things messy!!!!!!!!!!!!!!!!!!!!!

"""

class BiNode(object):
    def __init__(self):
        self.left = None
        self.right = None

# define a new linkedlist class will be more better, but not in python, coz python do not have return type
class DLinkedList(object):
    def __init__(self,root=BiNode()):
        t=root
        while t is not None:
            t = t.left
        self.head = t

        p =root
        while p is not None:
            p = p.right
        self.tail = p

        self.convert111(root) # convert root here will be better

    def convert111(self,root):
        """
        just convert the leaf node that is not head and tail
        inorder traversal
        if root is None: return None
        convert111(root.left)
        if root.left is not None and root.left is not head: concati(root.left, root)
        if root.right is not None and root.right is not tail: concati(root, root.right)
        convert111(root.right)
        """
        pass




def convert(root):
    """
    in place convert a tree to a double llist
    :param root:
    :return:
    """
    if not root:
        return [root,root] # return head and tail
    else:
        [h1,root.left]=convert(root.left)
        root.left.right = root         #root.right is not none, set link of root.left
        [root.right,t2]=convert(root.right)
        root.right.left = root
        return [h1,t2]

