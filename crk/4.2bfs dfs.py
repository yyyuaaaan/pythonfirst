"""__author__ = 'anyu'

4.2 Given a directed graph, design an algorithm to find out
whether there is a route between two nodes.

It may be worth discussing with your interviewer the trade-offs between breadth first search and depth
first search for this and other problems. For example, depth first search is a bit simpler to implement
since it can be done with simple recursion. Breadth first search can also be useful to find the shortest path,
whereas depth first search may traverse one adjacent node very deeply before ever going onto the immediate neighbors.
"""

from collections import deque

class Node(object):
    def __init__(self,data):
        self.data=data
        self.neighbours=[]
    def __str__(self):
        return str(self.data)

# if need to output route, can maintain a parent set outside the hasroute function
# parent = dict(), set() not gonna work, because we need to keep the parent node's address,
# dict can keep address in key/value pairs as value
# parent.update(n1,None)) (x,y),then output the as a linkedlist to indicate the route
#if (str(hash(node1)) + "," + str(hash(node2))) in cache2:
#        return cache2[(str(hash(node1)) + "," + str(hash(node2)))]


def routebfs(n1,n2):
    """
    bfs, my code is correct
    :param n1:
    :param n2:
    :return:
    show that one node or None node ,this code will also work
    """
    q=Queue.Queue  # enque, to the right side of the queue list, frontier as visiting set, as queue
    q.put(n1)      # do not need to maintain a frontier, the queue is automaticly frontier
    visited=set()

    while not q.empty():
        frontier = q.get() # this is not frontier, this is the first node of frontier
        if frontier not in visited:
            visited.add(frontier)
            if frontier == n2:
                return True
            else:
                for neighbor in frontier.neighbors:
                    if neighbor not in visited:
                        q.put(neighbor)
                        # parent.setdefault(neighbor, frontier)
    return False

def route(n1,n2, visited=set()):
    """
    route from n1 to n2 in directed graph
    :param n1:
    :param n2:
    :return: true or false
    dfs
    visited=set()    to avoid loop, if recursive dfs, visited set should be put outside or in the parameter

    """
    if not n1:
        return False
    else:
        for node in n1.neighbors:
            if node not in visited:
                visited.add(node)
                #parent.setdefault(neighbor,n1) must be setdefault, get DON"T change dictionary

                if node == n2:
                    return True
                else:
                    return route(node,n2,visited) # implicitly using stack

def hasroute(n1,n2):

    visited = set(n1)

    parent = dict()
    parent.get(n1,None)
    if route(n1,n2,visited) == True:
        n = n2
        print(n2)
        while parent.get(n) != None:
            print str(parent.get(n))
    return



    return route(n1,n2,set(n1))
