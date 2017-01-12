"""

__author__ = 'anyu'
2.2 Implement an algorithm to find the kth to last element of a singly linked list.

If the size of the linked list is known, then the kth to last element isthe (length - k)
solution is so trivial, we can almost be sure that this is not what the interviewer intended.
so assume lenth is not known
"""
class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def kthlast(l,k):
    '''
    iterative
    '''
    front = Node(None)
    front.nextnode=l

    if k<=0:return

    i = 0
    while i in range(k):

        if not front.nextnode:
            print "lenth not enough"
            return
        else:
            front=front.nextnode
            i+=1

    end = l
    while front.nextnode:
        front=front.nextnode
        end=end.nextnode
    return end
