"""
You have two very large binary trees: T1, with millions of nodes,
and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1
That is, if you cut off the tree at node n, the two trees would be identical.

note: tree mactching can be identical to string matching, 2 solutions, trade off between time and space
      string solution take more space and less time; tree recursion solution more time,less space

note: create algo, not code,! some questions are just design, do not need to code completely

Brute force method, for milliond nodes in T1, do a tree macth of T2  O(M*N) time
not right, coz rotation?

another approach be ctti 5th: (i think it may be wrong)
In this smaller, simpler problem, we could create a string representing the inorder and preorder traversals.
If T2's pre-order traversal is a substring of T l's pre-order traversal, and T2'sin-order traversal
is a substring of Tl's in-order traversal,then T2 isa subtree of Tl.
Substrings can be checked with suffix trees in linear time, so this algorithm is relatively
efficient in terms of the worst case time.

add '(' ')', and then do not need to two times traversal
"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)


def match(n1,n2):
    """
    if n1 match n2
    """
    if not n1 and not n2: return True
    elif not n1 or not n2: return False
    elif n1.data is not n2.data: return False
    else:
        return match(n1.left, n2.left) and match(n1.right, n2.right)

def subtree(t1,t2):
    """
    if t2 is a subtree of t1
    not bst, so have to check every node in t1 O(mn)
    """
    if not t2: return True
    elif not t1: return False
    elif t1.data is t2.data:
        if match(t1,t2): return True
    else:
        return subtree(t1.left,t2) or subtree(t1.right,t2)


    # two traversals
def inordertraversal(tree, inorderstr=[]):
    if not tree:
        return inorderstr
    else:
        inordertraversal(tree.left, inorderstr)
        inorderstr.append(tree.data)
        inordertraversal(tree.left, inorderstr)

def preordertraversal(tree, preordersttr=[])  :
    pass

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

    T1preorderstr=[]
    preordertraversal(T1millions, T1preorderstr)

    T2inorderstr=[]
    inordertraversal(T2hundreds, T2inorderstr)

    T2preorderstr=[]
    preordertraversal(T2hundreds, T2preorderstr)

    return  T2preorderstr in T1preorderstr and T2inorderstr in T1inorderstr