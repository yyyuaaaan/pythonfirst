"""

__author__ = 'anyu'

2.7 Implement a function to check if a linked list is a palindrome,
"""
# if do it as a linked list, push all data in a stack, than popup and compare

def ispalindrome(llist):
    if len(llist)<=1:
        return True
    elif len(llist)==2:
        return llist[0]==llist[1]
    else:
        return ispalindrome(llist[1:len(llist)-1])


def ispalindrome2(llist):
    ltemp=llist[:]
    llist.reverse()
    return llist == ltemp

# Iterative Approach is just push in to stack, which is implicitly recursive

print ispalindrome([1,2,3,4,5,4,3,2,1])

def ispalindrome3(lnodes):
    if not lnodes or lnodes.next is None:
        return True
    lstack = []
    dummy = None
    dummy.next = lnodes
    while dummy.next is not None:
        dummy = dummy.next
        lstack.append(dummy.data)

    dummy2= lnodes
    while lstack:
        if lstack.pop() is not dummy2.data:
            return False
        dummy2 = dummy2.next
    return True

def ispalindrome(array):

    # judge an array if it is palindrome
    if not array or len(array)==1:
        return True
    else:
        return ispalindrome(array[1:-1])

def ispalindromelist(llist):
    p = llist
    if not p or p.nextnode==None:
        return true
    else:
        l=[]
        while p:
            l.append(p.data)
            p=p.nextnode

        return ispalindrome(l)
