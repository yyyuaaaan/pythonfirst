"""

__author__ = 'anyu'

Implement an algorithm to delete a node in the middle
 of a singly linked list, given only access to that node.
 p1 is that node to be deleted
 p2 = p1.next
 p1.data = p2.data
 p1,next = p2.next
 del(p2)

 Note that this problem cannot be solved if the node to be deleted
 is the last node in the linked list. That's ok—your interviewer wants
 you to point that out, and to discuss how to handle this case. You could,
for example, consider marking the node as dummy.

"""

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.nextnode=None

def delnode(p, llist):
    if not p:
        print("null node")
        return
    elif p == llist:
        llist=llist.nextnode
        return llist
    elif p.nextnode== None:
        prepointer=llist
        while prepointer.nextnode is not p:
            prepointer=prepointer.nextnode
        prepointer.nextnode = None
        return llist
    elif p.nextnode.nextnode == None:
        p.data = p.nextnode.data
        p.nextnode=None
        return llist

    else:
        p.data=p.nextnode.data
        p.nextnode=p.nextnode.nextnode
        return llist