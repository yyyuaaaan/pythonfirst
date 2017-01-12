"""__author__ = 'anyu'

4.3 Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

One way to implement this is to use a simple root.insertNode(int v) method
This will indeed construct a tree with minimal height but it will not do so very efficiently.
Each insertion will require traversing the tree, giving a total cost of O(N log N) to the tree.

Alternatively, we can cut out the extra traversals by recursively using the createMinimalBST
method. This method is passed just a subsection of the array and returns the


Although this code does not seem especially complex, it can be very easy to make little off-by-one errors.
Besure to test these parts of the code very thoroughly  (But I DID NOT! ONE TIME FINISHED MASTERPIECE:) )

discuss that it automatically maintain a binary SEARCH tree here
because it is orderd array, the mid point should be the root
"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return "<" +str(self.left) + "<" +str(self.data) + ">" + str(self.right) + ">"

def minheighttree(l):
    if not l:
        return Node(None)
    else:
        mid = len(l)/2-1
        temp = Node(l[mid])
        temp.left = minheighttree(l[mid:])
        temp.right = minheighttree(l[:mid])
        return temp
