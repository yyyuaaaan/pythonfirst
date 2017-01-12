"""

__author__ = 'anyu'

Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
import itertools

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.nextnode=None

linkedlist=Node()


def removedup(l):
    """
    current to loop the list
    runner to delete dups
    :param l:
    :return:
    """
    current = l
    while current:
        runner = current
        while runner.nextnode:
            if runner.nextnode.data == current.data:
                runner.nextnode=runner.nextnode.nextnode
            else:
                runner = runner.nextnode

        current=current.nextnode
    return

def removedupwithbuffer(l):
    """
    no extra buffer
    This code runs in 0(1) space, but 0(N2) time.
    """
    d={}
    i=0
    pre = Node(None)
    current = l

    while current:
        if current.data not in d.values():
            d[i] = current.data
            i+=1
            pre = current
        else:
            pre.nextnode = current.nextnode

        current=current.nextnode
    return
