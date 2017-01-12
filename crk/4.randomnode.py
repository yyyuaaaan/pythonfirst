# Random Node: You are implementing a binary search tree class from scratch, which, in addition
# to insert, find, and delete, has a method getRandomNode() which returns a random node from
# the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the met

#traverse numberofnodes
# random=x
# randomtraverse again

import random
r= random.randint(1, size) # random from 1 to size including both ends

class Node(object):
    def __init__(self,data, size=1):
        self.data=data
        self.left = None
        self.right = None
        self.size = size

    def insert(self, load):

        if self.data == load: # if with repetition is ok, no need for this line
            print "find data"
            return
        elif self.data> load:
            if not self.left:
                self.left = Node(load)
                self.size+=1 # important recursive stuff
            else:
                self.insert(self.left)
        else:
            if not self.right:
                self.right=Node(load)
                self.size+=1 # important recursive stuff
            else:
                self.insert(self.right)
        return

    def getRandomNode(self):
        """
        this func do too many randoms, we can get a rapper Tree class, and hold just one randomnumber
        o(logn), if we traverse two times, then, o(n)
        :return:
        """
        if self.left:
            leftsize=self.left.size
        else:
            leftsize =0
        if self.right:
            rightsize=self.right.size
        else:
            rightsize = 0
        d= leftsize+rightsize+1
        r= random.randint(1, d)
        if r ==d:
            return self
        elif r<= leftsize:
            self.left.getRandomNode(self)
        else:
            self.right.getRandomNode(self)

################################
        # to optimize, don't call random repetitively, get a ith node function
        # add getithnode in Node class, then add a getRandomnode in a wrapper Tree class
    def getithnode(self,i):

        if self.left:
            leftsize=self.left.size
        else:
            leftsize =0
        if self.right:
            rightsize=self.right.size
        else:
            rightsize = 0

        if i ==self.size:
            return self
        elif i<=leftsize:
            self.left.getithnode(i)
        else:
            self.right.getithnode(i-rightsize-1)
