"""

__author__ = 'anyu'

Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.

map addr to hash table
以地址为哈希表的键值，每出现一个地址，就将该键值对应的实值置为true。
那么当某个键值对应的实值已经为true时，说明这个地址之前已经出现过了， 直接返回它就OK了。

python do not support address or linkedlist

"""

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def circularnode(llist):
    #treat list index as pointer in c++, also as address
    p = llist
    hashtable=[]
    if not p: return
    while p:
        if hash(p) not in hashtable:
            hashtable.append(hash(p))
            p=p.nextnode
        elif hash(p) in hashtable:
            return p
    if not p:
        print("no circular")
        return


