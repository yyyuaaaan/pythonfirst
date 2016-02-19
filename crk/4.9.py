"""__author__ = 'anyu'
You are given a binary tree in which each node contains a value.
Design an algorithm to print all paths which sum up to that value.
Note that it can be any path in the tree - it does not have to start
at the root.
Design an algorithm :not coding completely

方案1：如果结点中包含指向父亲结点的指针，那么，只需要去遍历这棵二叉树， 然后从每个结点开始，不断地去累加上它父亲结点的值直
到父亲结点为空(这个具有唯一性， 因为每个结点都只有一个父亲结点。也正因为这个唯一性， 可以不另外开额外的空间来保存路径)，
如果等于给定的值sum，则打印输出。打印输出时，只需要提供当前结点的指针，及累加的层数即可。然后从当前结点开始， 不断保存其父亲
结点的值(包含当前结点)直到达到累加层数，然后逆序输出即可。看起来简单，但是没有考虑两个子节点之间的节点。

方案2：如果结点中不包含指向父亲结点的指针，则在二叉树从上向下查找路径的过程中， 需要为每一次的路径保存中间结果，累加求和仍然是
从下至上的，对应到保存路径的数组， 即是从数组的后面开始累加的，这样能保证遍历到每一条路径。
方案1和方案2的本质思想其实是一样的，不同的只是有无指向父亲结点的指针这个信息。 如果没有这个信息，则需要增加许多额外的空间来
存储中间信息。

Note that we don't stop traversing that path just because we found the sum. Why? • q = {2, 3, -4, -2, 6}
Now, what if the path can start anywhere? In that case, we can make a small modification. On every node, we look "up"
to see if we've found the sum. That is, rather than asking "Does this node start a path with the sum?," we ask,"Does
this node complete a path with the sum?"
When we recurse through each node n, we pass the function the full path from root to n.
This function then adds the nodes along the path inverse order from n to root.
When the sum of each subpath equals sum, then we print this path.

"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

def findsum(node, sum):
    """
    has a parent node
    :param node:
    :param sum:
    :return:
    """
    if not node: return
    p=node
    temp = 0
    pathtemp=[]
    while p:
        temp += p.value
        pathtemp.append(p)
        if temp == sum:
            print pathtemp # reverse order of one path
        p = p.parent

    #Search nodes beneath this one
    findsum(node.left, sum)
    findsum(node.right, sum)


def findsum(node, sum, path=[], depth=0):
    if not node: return

    #Insert current node into path.
    path.append(node.value)

    # Look up to see if there are paths end up with this node and sum to the given value
    temp = 0
    for i in range(depth, -1, -1):
        temp += path[i]
        if temp == sum:
            print path[i:]

    #Search nodes beneath this one
    findsum(node.left, sum, path, depth+1)
    findsum(node.right, sum, path, depth+1)

def findsum(node, sum, path=[]):
    """
    depth not needed
    :param node:
    :param sum:
    :param path:
    :return:
    """
    if not node: return

    #Insert current node into path.
    path.append(node.value)

    # Look up to see if there are paths end up with this node and sum to the given value
    temp = 0
    for i in range(len(path)-1, -1, -1):
        temp += path[i]
        if temp == sum:
            print path[i:]

    #Search nodes beneath this one
    findsum(node.left, sum, path)
    findsum(node.right, sum, path)