"""

__author__ = 'anyu'

2.7 Implement a function to check if a linked list is a palindrome,
"""
# if do it as a linked list, push all data in a stack, than popup and compare

def ispalindrome2(l):
    """
    reverse and compare: stack
    to optimize, only compare half of the reverse by sizeofstack/2.
    :param l:
    :return:
    """
    if not l:
        return True
    stack =[]

    p=l
    while p:
        stack.append(p.data)
        p=p.nextnode

    p2=l
    while p2:
        if p2.data != stack.pop():
            return False
        else:
            p2=p2.nextnode
    return True

# Iterative Approach is just push in to stack, which is implicitly recursive


def ispalindrome(array):

    # judge an array if it is palindrome
    if not array or len(array)==1:
        return True
    else:
        return ispalindrome(array[1:-1])
