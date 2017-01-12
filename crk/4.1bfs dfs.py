"""__author__ = 'anyu'
4.2 Given a directed graph, design an algorithm to find out
whether there is a route between two nodes.

It may be worth discussing with your interviewer the trade-offs between bfs and dfs for this and other problems.
For example, dfs is a bit simpler to implement since it can be done with simple recursion. bfs can also be useful
to find the shortest path,whereas depth first search may traverse one adjacent node
very deeply before ever going onto the immediate neighbors.
"""

class Node(object):
    def __init__(self,data):
        self.data=data
        self.neighbours=[]
    def __str__(self):
        return str(self.data)
from collections import deque

def routebfs(n1,n2):
    """
    from n1 to n2
    if need to output route, can maintain a parent set outside the hasroute function
    parent = dict()
    parent[n1]=None
    then reverse output from n2 to n1 the path in to a deque.
    """
    visited=set()
    q=deque()
    q.append(n1) # the q is just frontier ie the visiting set

    while q:
        x = q.popleft()
        if x == n2:
            return True
        elif x not in visited:
            visited.add(x)
            for n in n1.neibors:
                q.append(n)   #parent[n]=x
        elif x in visited:
            print "loop"
            return False
    return False

def routedfs(n1,n2, visited=set()):
    """

    """
    if n1==n2:
        return True
    else:
        visited.add(n1)
        for x in n1.neibors:
            if x in visited:
                return False
            elif routedfs(x,n2):
                return True
        return False

def hasroute(n1,n2):
    visited = set(n1)

    if route(n1,n2,visited) == True:
        n = n2
        print(n2)
        while parent.get(n) != None:
            print str(parent.get(n))
    return

