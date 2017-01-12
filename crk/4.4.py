import Queue
"""__author__ = 'anyu'
Given a binary tree, design an algorithm which creates a linked list of all the nodes at
each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

tweak the bfs

"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
# visited = set() # visited binary tree DO NOT need visited set, because must not have loop
# O(N) time and space, bfs

def bfs_to_list(tree):   # here tree parameter is just another node,recursively defined, as an pointer
    if not tree:
        return [[]]

    result = [[tree]]
    queue = [tree]

    while queue:
        nextlevelqueue = [] #go to next level
        for node in queue:
            if node.left: nextlevelqueue.append(node.left)
            if node.right: nextlevelqueue.append(node.right)

        result.append(nextlevelqueue) # or: result.append([node for node in queue]),this is hardcopy:

        queue = nextlevelqueue


def bfs(tree):
    if not tree:
        return
    else:
        q=Queue.Queue()
        q.put(tree)
        layersize = q.qsize()
        layernumber = 0
        result = [[None]*10] #max layers 10

        while not q.empty():

            while layersize >0:
                node=q.get()
                result[layernumber].append(node)
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
            layersize = q.qsize()
            layernumber +=1



"""
>>> s=[2,3]
>>> d=[1,4]
>>> s.append(d)
>>> s
[2, 3, [1, 4]]
>>> d
[1, 4]

"""
