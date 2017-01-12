# Build Order: Topological order
# You are given a list of projects and a list of dependencies

# (which is a list of pairs of projects,wherethesecondprojectisdependentonthe rstproject).
# Allofaproject'sdependencies must be built before the project is. Find a build order that
# will allow the projects to be built. If there is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output:f, e, a, b, d, c

# if input is a graph, lists, then i can use dfs; be careful cycles, mark visited to solve is or
#  hashtable to detect loop first

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=Node

def buildorder(dependency):
    """
    dependency is a dict
    projectslist is a list
    :param graph:
    :return:
    actually linear time O(p+d)

    if
    """
    topologylist=[]

    i=0
    n= dependency.size()
    while i < n:
        for x in dependency.keys():
            if x not in dependency.values():
                topologylist.append(x)
                del(dependency[x])
        i+=1

    if dependency:
        print "no solution, loop"
        return
    else:
        return topologylist
