"""

__author__ = 'anyu'

2.2 Implement an algorithm to find the kth to last element of a singly linked list.

If the size of the linked list is known, then the kth to last element isthe (length - k)
solution is so trivial, we can almost be sure that this is not what the interviewer intended.
so assume lenth is not known
"""


def kthlast2(k,llist):  # singly linked list, here using a stack, so it is implicitly using recursion
                        #Each of these recursive solutions takes 0 ( n ) space due to the recursive calls.
    tempstack=[]
    for x in llist:
        tempstack.append(x)
    for count in range(k):
        temp = tempstack.pop()
    return  temp

"""
Solution #3: Iterative
A more optimal, but less straightforward, solution is to implement this
 iteratively.We can use two pointers, pi and p2. Weplace them k nodesapart
  in the linked list by putting pi at the beginning and moving p2 k nodes
   into the list.Then, when we move them at the same pace, p2 will hit the end
   of the linked list after LENGTH - k steps. At that point, pi will be LENGTH -
   k nodes into the list, or k nodes from the end.

"""
def kthlast3(k,llist):  # Iterative
    if (k in range(len(llist))) ==False:
        print "out of bounds"
        return
    else:
        p1=0    # pointer 1
        p2=k-1  # iteratively p2 goto k-1
        while p2 < len(llist)-1:   # if p2.next != null then p2=p2.next
            p2+=1
            p1+=1
        return llist[p1]  #

def lastkth(k,linkedlist):
    if not linkedlist:
        print "list empty"
        return
    elif linkedlist.next is None:
        if k ==1:
            return linkedlist
        else:
            print("no such result")
            return

    else:
        current = linkedlist
        rider = current.nextnode
        i= k-1
        while i>=0:
            if rider.nextnode is None:
                print("no such result")
            else:
                rider=rider.nextnode

        while rider.nextnode is not None:
            rider=rider.nextnode
            current=current.nextnode

        return current

print  kthlast(5,[1,2,3,4,5,8,5,6])

print kthlast2(5,[1,2,3,4,5,8,5,6])
print kthlast3(5,[1,2,3,4,5,8,5,6])


class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def kthtolastbetter(kth, llist):
    if llist is None return "no data in list"
    stacklist=[]
    pointer = llist
    stacklist.append(pointer.data)
    while pointer.next is not None:
        pointer = pointer.next
        stacklist.append(pointer)
    for i in range(k):
        if stacklist is None: return "k overbound"
        else:
            t= stacklist.pop()
    return t