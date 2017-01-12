"""

__author__ = 'anyu'

Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
EXAMPLE
Input: A -> B -> C -> D -> E -> C [thesameCasearlier] Output: C

map addr to hash table
python do not support address or linkedlist use hash()

"""

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def circularnode(l):
    hashset=set()
    p=l
    while p:
        if hash(p) not in hashset:
            hashset.add(hash(p))
        else:
            return p
        p=p.nextnode

    print 'no loop'
    return
