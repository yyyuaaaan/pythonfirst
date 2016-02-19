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

def remove_dup(linkedlist):
    """
    use list as linkedlist in python
    use dict as hash table
    """
    hashtable=[]
    if not linkedlist or linkedlist.nextnode is None:
        return linkedlist
    else:
        prerider= linkedlist
        rider = prerider.nextnode
        hashtable.append(prerider.data)
        while rider.nextnode is not None:
            if rider.data in hashtable:
                prerider.nextnode=rider.nextnode
                rider=prerider.nextnode
            else:
                hashtable.append(rider.data)
                rider=rider.nextnode
                prerider=prerider.nextnode

        if rider.data in hashtable:
            prerider.nextnode=None
        return linkedlist


def remove_dup2(linkedlist):
    """
    no extra buffer
    if make yourself a python linked list, it will be very cumbersome.
    trade off between time and space, and also readability, maintainability

    assume linkedlist is a list() in python
    assume current and rider are pointers of linkedlist
    if define a new Node class, new space, less efficient than official python

    This code runs in 0(1) space, but 0(N2) time.
    """

def removdup(linkedlist):
    if not linkedlist or linkedlist.nextnode == None:
        return linkedlist
    else:
        current = linkedlist
        rider=current.nextnode
        prerider=current
        while current.nextnode is not None:
            while rider.nextnode is not None:
                if rider.data ==current.data:
                    prerider.nextnode=rider.nextnode # use prerider to del the current rider node
                    rider = prerider.nextnode
                else:
                    rider=rider.nextnode
                    prerider=prerider.nextnode
            if rider.data == current.data:
                prerider.nextnode = None

            current= current.nextnode
    return linkedlist





#print remove_dup([1,2,3,4,4,'sfd',5,5,5,7])

#print remove_dup2([1,2,3,4,4,5,5,5,7])
