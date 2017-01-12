"""__author__ = 'anyu'

Paths Sum count: You are given a binary tree in which each node contains an POS OR NETinteger value
 Design an algorithm to count the number of paths that sum to a given value.
 The path does not need to start or end at the root or a leaf, but it must go downwards
A: from parent nodes to child nodes
B: ANY ROUTE

Paths Sum routes,ANY ROUTE: You are given a binary tree in which each node contains a value.
Design an algorithm to print all paths which sum up to that value.

Note that we don't stop traversing that path just because we found the sum. Why? Since neg numbers.

"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

# from current upwards, return counts
def countPathSum(t, sum, count=0, pathcache=[]):
    if not t:
        return count
    else:
        pathcache.append(t.data)
        count += countsOfPathEndsatNode(sum,pathcache)
        return countPathSum(t.left) + countPathSum(t.right)
def countsOfPathEndsatNode(sum, llist):
    count=0
    temp=0
    for x in llist:
        temp+=x
        if temp == sum:
            count+=1
    return count

# from current downwards, return counts
def countPathSum(t,sum):
    if not t:
        return 0
    else:
        temp = countFromNode(t, sum)
        return temp+countPathSum(t.left,sum)+countPathSum(t.right,sum)
def countFromNode(t, sum, currentSum=0):
    if not t:
        return 0
    else:
        count = 0
        currentSum+= t.data
        if currentSum ==sum:
            count +=1
        return count + countFromNode(t.left, sum, currentSum) +countFromNode(t.right, sum, currentSum)

# print all paths, from root to all innernode
def findsum(node, sum, path=[]):
    if not node: return

    #Insert current node into path.
    path.append(node.value)

    # Look up to see if there are paths end up with this node and sum to the given value
    temp = 0
    for i in range(len(path)-1, -1, -1):
        temp += path[i]
        if temp == sum:
            print path[i:]

    findsum(node.left, sum, path)
    findsum(node.right, sum, path)

# print all root to leaf paths
def findRoottoLeafPaths(t, suminput, l=[]):
    if not t: return
    else:
        l.append(t.data)
        if not t.left and not t.right:
            if sum(l) ==suminput:
                print l
        else:
            findRoottoLeafPaths(t.left, suminput, l)
            findRoottoLeafPaths(t.right, suminput, l)

#Given a binary tree, find the maximum path sum.
def maximumSum(t,maxtemp=-10000):
    if not t:
        return maxtemp
    else:
        return max(maxtemp, maxSumFromRoot(t.left),maxSumFromRoot(t.right))

def maxSumFromRoot(t,sumtemp=0, maxtemp= -10000):
    if not t:
        return maxtemp
    else:
        sumtemp+= t.data
        maxtemp = max(sumtemp,maxtemp)
        return max(maxtemp, maxSumFromRoot(t.left), maxSumFromRoot(t.right))
