"""

__author__ = 'anyu'

You have two numbers represented by a linked list, where each node contains a
singledigit.The digits are stored in reverse order,such that the 1's digit is at the head
of the list. Write a function that adds the two numbers and returns the sum as a
linked list.
Input:
  First List: 7->5->9->4->6  // represents number 64957
  Second List: 8->4 //  represents number 48
Output
  Resultant list: 5->0->0->5->6  // represents number 65005

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
  Ex:123 1->2->3
10234 1->0->2->3->4
ans: 10357 1->0->3->5->7

stack input list;
stack result list; need to creat an extra stack, then build a linked list of result
or insert result in front of the list
"""

def addlistforwardorder(l1,l2):
    # using stacks, pretend not list, but linkedlist

    l1tempstack=[]
    l2tempstack=[]
    if len(l1)>len(l2): l2tempstack+=[0]*(len(l1)-len(l2))
    if len(l2)>len(l1): l1tempstack+=[0]*(len(l2)-len(l1))

    for x in l1: l1tempstack.append(x)
    for x in l2: l2tempstack.append(x)

    ltemp = []
    while l1tempstack != []:
        ltemp.append(l1tempstack.pop()+l2tempstack.pop())

    for p1 in range(len(ltemp)):
        if ltemp[p1]>9:
            ltemp[p1] -= 10
            ltemp[p1+1] +=1   # do  maintain carry implicitly

    return ltemp



print addlistforwardorder([1,2,3,4],[1,2,9])
print addlistforwardorder([4,3,2,1],[9,2,1])

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

import Queue


def addnumberlistreverse(l1,l2):
    """
    must use queue to make it clear, if not, will have cumbersome details to deal with
    :param l1: input list
    :param l2:
    :return: list of result
    """
    q1=Queue.Queue()
    q2=Queue.Queue()
    if not l1 and not l2:
        print("null input")
        return
    else:
        p = l1
        while p:
            q1.put(p.data)
            p=p.nextnode

        p=l2
        while p:
            q2.put(p.data)
            p=p.nextnode

    result = Node()
    p=Node() # first node dummy node, need to delete before return the result
    carry=0
    while not q1.empty() and not q2.empty():
        digit1=q1.get()
        digit2=q2.get()
        tempdigit= (digit1+digit2+carry)%10
        carry=(digit1+digit2+carry)/10
        tempnode=Node(tempdigit)
        p.nextnode= tempnode
        p=p.nextnode

    while not q1.empty():
        digit=q1.get()
        tempdigit = (digit+carry)%10
        carry = (digit+carry)/10
        tempnode=Node(tempdigit)
        p.nextnode=tempnode
        p=p.nextnode


    while not q2.empty():
        digit=q2.get()
        tempdigit = (digit+carry)%10
        carry = (digit+carry)/10
        tempnode=Node(tempdigit)
        p.nextnode=tempnode
        p=p.nextnode

    #del dummy node of result
    result=result.nextnode

    return result



def addlistforwardorder(l1,l2):
    if not l1 and not l2:
        print("null input")
        return

    stack1=[]
    stack2=[]

    p= l1
    while p:
        stack1.append(p.data)
        p=p.nextnode

    p = l2
    while p:
        stack2.append(p.data)
        p=p.nextnode

    carry = 0
    resultstack=[]
    while not len(stack2)==0 and not len(stack1)==0:
        digit1=stack1.pop()
        digit2=stack2.pop()
        resultstack.append((digit1+digit2+carry)%10)
        carry = (digit1+digit2+carry)/10

    while not len(stack1)==0:
        digit1=stack1.pop()
        resultstack.append((digit1+carry)%10)
        carry = (digit1+carry)/10

    while not len(stack2)==0:
        digit2=stack2.pop()
        resultstack.append((digit2+carry)%10)
        carry = (digit2+carry)/10

    # creat result linkedlist
    result=Node()
    p=result
    while not len(resultstack)==0:
        temp= resultstack.pop()
        tempnode= Node(temp)
        p.nextnode=tempnode
        p=p.nextnode
    #del dummy first node
    result = result.nextnode

    return result

