"""

__author__ = 'anyu'

You have two numbers represented by a linked list, where each node contains a
single digit.The digits are stored in reverse order,such that the 1's digit is at the head
of the list. Write a function that adds the two numbers and returns the sum as a
linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output:2 -> 1 -> 9.Thatis,912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
  Ex:123 1->2->3
10234 1->0->2->3->4
ans: 10357 1->0->3->5->7

stack input list;
stack result list; need to creat an extra stack, then build a linked list of result
or insert result in front of the list
"""

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def sumlistreverse(l1,l2):
    p1=l1
    p2=l2
    carry = 0

    res=Node(None)

    while p1 and p2:
        d= p1.data+p2.data
        num= (d+carry)%10
        carry=(d+carry)/10

        res.nextnode=Node(num)
        p1=p1.nextnode
        p2=p2.nextnode

    while p1:
        d= p1.data
        num= (d+carry)%10
        carry=(d+carry)/10
        res.nextnode=Node(num)
        p1=p1.nextnode

    while p2:
        d= p2.data
        num= (d+carry)%10
        carry=(d+carry)/10
        res.nextnode=Node(num)
        p2=p2.nextnode

    return res.nextnode



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

