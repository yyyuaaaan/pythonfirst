"""
Check Subtree
You have two very large binary trees: T1, with millions of nodes,and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of T1
That is, if you cut off the tree at node n, the two trees would be identical.
subtree is Not in the internal of t1, but just exact subtree of t1 ==t2

1
Brute force method, for milliond nodes in T1, do a tree macth of T2
rotation means diffs structure.
recursion. time is worst case O(M*N) time, but closer to O(n + km) k is the occurances of root of m, and even lesser
space is O(logn + logm) trading time with space.

2
inorder traverl of string compare not gonna work, for example, two bst with different structure of[1,2,3]
will always print the same array, but they are different tree
for the same reason, preorder traversal also not working
but, add '(' ')', when we do inorder traversal
Or, we can compare inorder AND preorder traversal, then gonnawork
Substrings can be checked with suffix trees in linear time. O(m+n) space and time

"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

def isMatch(t1,t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    elif t1.data == t2.data:
        return isMatch(t1.left, t2.left) and isMatch(t1.right, t2.right)
    else:
        return False

def subtree(t1,t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    else:
        return t1.data == t2.data and ( subtree(t1.left,t2) or subtree(t1.right, t2) )


    # two traversals
def inordertraversal(tree, inorderstr=[]):
    if not tree:
        return inorderstr
    else:
        inordertraversal(tree.left, inorderstr)
        inorderstr.append('(')
        inorderstr.append(tree.data)
        inorderstr.append(')')
        inordertraversal(tree.left, inorderstr)

def subtree(T1millions,T2hundreds):
    """
    this is alternative solution,simple solution is the one above
    Analyzing the runtime is somewhat complex. A naive answer would be to say that it is 0(nm) time,
    When might the simple solution be better, and when might the alternative approach be better?
    This is a great conversation to have with your interviewer
    The simple solution takes 0(n + m) memory. The alternative solution takes 0(log(n) + log(m)) memory.
    The simple solution is 0(n + m) time and the alternative solution has a worst case time of 0(nm).
    """
    T1inorderstr=[]
    inordertraversal(T1millions, T1inorderstr)

    T2inorderstr=[]
    inordertraversal(T2hundreds, T2inorderstr)

    return T2inorderstr in T1inorderstr
