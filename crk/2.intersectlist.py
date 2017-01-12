# Time:  O(m + n)
# Space: O(1)
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 - a2
#                    \
#                      c1 - c2 - c3
#                    /
# B:     b1 - b2 - b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
# Definition for singly-linked list.
class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode = None


def intersectlist(l1,l2):
    """
    hasset O(M+N)
    :param l1:
    :param l2:
    :return:
    """
    p1=l1
    hashtable=set()
    while p1:
        hashtable.add(hash(p1))
        p=p.nextnode

    p2=l2
    while p2:
        if p2 in hashtable:
            return p2
        else:
            p2=p2.nextnode
    print "no intersect"
    return


def intersectlist2(l1,l2):
    """
    no extra space
# 1. Run through each linked list to get the lengths and the tails.
# 2. Compare the tails. If they are dierent (by reference, not by value), return immediately. There is no inter
# section.
# 3. Set two pointers to the start of each linked list.
# 4. Onthelongerlinkedlist,advanceitspointerbythedi erenceinlengths.
# 5. Now, traverse on each linked list until the pointers are the same.

    """
    #get tails and len

    len1=0
    p1=l1
    while p1:
        len1+=1
        if not p1.nextnode:
            tail1=p1
        p1=p1.nextnode

    len2=0
    p2=l2
    while p2:
        len2+=1
        if not p2.nextnode:
            tail2=p2
        p1=p1.nextnode

    if tail1 !=tail2:
        print "no intersect"
        return
    else:
        if len1==len2:
            return getintersect(l1,l2)
        elif len1>len2:
            mov=len1-len2
            temp=Node(None)
            temp.nextnode=l1
            while mov>0:
                temp=temp.nextnode
            return getintersect(temp,l2)
        elif len2>len1:
            mov=len2-len1
            temp=Node(None)
            temp.nextnode=l2
            while move>0
                temp=temp.nextnode
            return getintersect(l1,temp)

