"""

__author__ = 'anyu'

Write code to partition a linked list around a value x,
such that all nodes less than x come before alt nodes
 greater than or equal to x.

 If this were an array, we would need to be careful about how
  we shifted elements. Array shifts are very expensive.
However, in a linked list, the situation is much easier. Rather than shifting
and swapping elements, we can actually create two different linked lists:
one for elements less than x, and one for elements greater than or equal to x.
We iterate through the linked list, inserting elements into our before
list or our after list. Once we reach the end of the linked list and
have completed this splitting, we merge the two lists.

filter: we trade less efficiency to less bugs and debugging time

"""

def parti(l,n):
    dummy=Node(None)
    dummy.nextnode = l

    p = l

    while p.nextnode:
        if p.nextnode.data <=n:
            # move to front
            temp = p.nextnode
            p.nextnode=p.nextnode.nextnode
            temp.nextnode=dummy.nextnode
            dummy.nextnode=temp

        p=p.nextnode
    return


class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def partitioned(value,llist):
    greaterorequalvaluelist=None
    gpointer=None
    lessvaluelist=None
    lpointer=None
    if not llist:
        print "null list"
        return
    else:
        p=llist
        while p:
            if p.data >= value:
                temp=Node(p.data)
                if not greaterorequalvaluelist:
                    greaterorequalvaluelist = temp
                    gpointer = temp
                else:
                    gpointer.nextnode= temp
                    gpointer=gpointer.nextnode
            else:
                temp = Node(p.data)
                if not lessvaluelist:
                    lessvaluelist = temp
                    lpointer = temp
                else:
                    lpointer.nextnode = temp
                    lpointer = lpointer.nextnode
            p=p.nextnode

        p2= lessvaluelist
        while p2.nextnode:
            p2 = p2.nextnode
        p2.nextnode = greaterorequalvaluelist

        print "partition the list such that value less then value input comes before nodes value " \
              "greater then value"
        return lessvaluelist


def partitioned(value,array):
    i=0
    j=len(array)-1

    while i < j:
        if array[i]< value:
            i +=1
        elif array[j]>= value:
            j-=1


        elif array[i]>=value and array[j]< value:
            array[i],array[j] =array[j], array[i]
            i +=1
            j-=1

    return array
