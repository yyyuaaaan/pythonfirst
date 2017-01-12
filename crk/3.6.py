
"""
__author__ = 'anyu'

Write a program to sort a stack in ascending order. You should not make any assumptions
about how the stack is implemented. The following are the only functions that should be
used to write this program: push | pop | peek | isEmpty.

1,insertion sort, use one helping stack, keep the reversed result in temp stack, then insert one by one
2, selection sort, need two extra stack, one keep orderd result, one to maintain min.
3,priority queue, until all
4 use list as linked list, to do selection sort, or make a  linked list by myself

"""

import Queue

def psort(s):
    if not s:
        print("stack empty")
        return
    else:
        pqueque = Queue.PriorityQueue()
        while not s.isEmpty():
            data = s.pop()
            pqueque.put(data)

        while not pqueque.empty():
            data = pqueque.get()
            s.push(data)

        return s



def stacksort(s):
    """
     15
    2 4
    5 2
    7 1
    insertion sort
    1,insertion sort, use one helping stack, keep the reversed result in temp stack, then insert one by one

    """
    temp=[]
    if not s:
        return
    else:
        temp.append(s.pop())
        #insertion
        while s:
            if s.peek()>= temp.peek():
                temp.append(s.pop())
            else:
                item = s.pop()
                while item<temp.peek():
                    s.push(temp.pop())
                temp.append(item)
        return
