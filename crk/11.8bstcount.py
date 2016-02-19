"""__author__ = 'anyu'
11.8 Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a
number x (the number of values less than or equal to x). Implement the data structures and algorithms to support
these operations. That is,implement the method track(int x), which is called when each number is generated, and the
method getRankOfNumber (int x), which returns the number of values less than or equal to x (not including x itself).

1 naive, use array, costly, when inserting
2 bst:
Instead of inserting elements into an array, we insert elements into a binary search tree.
The method track(int x) will run in O(log n) time
To find the rank of a number, we could do an in-order traversal, keeping a counter as we traverse.
The goal is that, by the time we find x, counter will equal the number of elements less than x.

As long as we're moving left during searching for x, the counter won't change. Why? Because all the values we're skipping
on the right side are greater than x. After all, the very smallest element (with rank of 1) is the leftmost node.

When we move to the right though, we skip over a bunch of elements on the left. All of these elements are less
than x, so we'll need to increment counter by the number of elements in the left subtree.


Rather than counting the size of the left subtree (which would be inefficient),
we can track this information as we add new elements to the tree.

Recursively, the algorithm is the following:
 int getRank(Node node, :nt x) {
           if x is node.data
                return node.leftSizeQ
           if x is on left of node
                return getRank(node.left, x)
           if x is on right of node
                return node.leftSizeQ + 1 + getRank(node.right, x)
}
Note how we've handled the case in which d is not found in the tree. We check for the -1 return value, and,
when we find it, return -1 up the tree. It is important that you handle cases like this.
"""

class Node:
    """docstring for Node"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.numLeftChildren = 0

class BSTree:
    def __init__(self):
        # initializes the root member
        self.root = None

    def addNode(self, data):
        # creates a new node and returns it; this is add new root node, insert is insert on a tree
        return Node(data)

    def insert(self, root, data):   # just track
        """
        first consider the root is None, then when do recursion, do not need to consider left or right is None
        """
        if root == None:
            # it there isn't any data
            # adds it and returns
            return Node(data)
        else:
            # enters into the tree
            if data <= root.data:
                root.left = self.insert(root.left, data)
                root.numLeftChildren += 1
            else:
                # processes the right-sub-tree
                root.right = self.insert(root.right, data)
            return root

    def getRankOfNumber(self, root, num):
        if root == None:
            return 0
        else:
            if num == root.data:
                return root.numLeftChildren
            if num < root.data:
                return self.getRankOfNumber(root.left, num)
            if num > root.data:
                return self.getRankOfNumber(root.right, num) + root.numLeftChildren + 1

# main
btree = BSTree()
root = btree.addNode(13)
btree.insert(root, 3)
btree.insert(root, 14)
btree.insert(root, 1)
btree.insert(root, 4)
btree.insert(root, 18)
btree.insert(root, 2)
btree.insert(root, 12)
btree.insert(root, 10)
btree.insert(root, 5)
btree.insert(root, 11)
btree.insert(root, 8)
btree.insert(root, 7)
btree.insert(root, 9)
btree.insert(root, 6)

print btree.getRankOfNumber(root, 8)