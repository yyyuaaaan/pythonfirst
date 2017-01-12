# BST Sequences:A binary search tree was created by traversing through an array
# from left to right and inserting each element. Given a binary search tree with
#     distinct elements, print all possible arrays that could have led to this tree.
# 2 1 3
# 2 3 1
# a bit wrong with this problem, all permutations can create this bst, but the problem is only focusing on
# the  traversel that root printed out first
# this sequences is such that by scan and creat the tree, only insert on the leaf nodes of the tree

class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode = None

def bst_seq(t, res=[]):
    """
    res should not be [], just when call the function, let res=[] bst_seq(tree,[]), then OK
    """

    if not t:
        return  res
    else:
        l = bst_seq(t.left)
        r = bst_seq(t.right)
        for x in l:
            for y in r:
                # keep seperate relative order of x and y, then weave x and y, then add prefix
                for z in weaving(x, y):
                    # z  is one weaving of the array x and y
                    res.append([t.data]+z)
        return res

def weaving(x,y, temp=[]):
    """
    weaving two array
    """
    if not x:
        temp.append(y)
        return temp
    elif not y:
        temp.append(x)
        return temp
    else:
        for t in weaving(x[1:],y,temp):
            temp.append([x[0]+ t])

        for p in weaving(x, y[1:],temp):
            temp.append([y[0]+p])
        return temp



