"""__author__ = 'anyu'
List of Depths:
Given a binary tree, design an algorithm which creates a linked list of all the nodes at
each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

tweak the bfs
# O(N) time and space, bfs and dfs, yet dfs takes extra logN space

"""

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

def bfs_to_list(tree):
    if not tree:
        return []
    else:
        currentq=[]
        currentq.append(tree)
        nextq=[]
        res = []

        while currentq:
            res.append([currentq]) # or put nextq here, then no need to update
            for item in currentq:
                if item.left:
                    nextq.append(item.left)
                elif item.right:
                    nextq.append(item.right)
            if nextq: # check if has next layer
                currentq = nextq
                nextq =[]
            else:
                return res

def dfs(t,res=[],level=0):
    if not t:
        return
    elif level ==len(res):
        # new level result to create
        # first time to traverse this level
        res.append([t])
    else:
        res[level].append(t)
    dfs(t.right,res,level+1)
    dfs(t.left,res,level+1)

