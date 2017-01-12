
# this is finding wheather a route between n1 and n2, no parent route
# if bst, then

def findOnBst(t, n1, n2):
    '''
    requrire n1< n2.data
    and t, n1, n2 not null, n1!=n2.data
    n1, n2 already in tree
    '''
    if n2.data== t.data or t.data == n1.data:
        return True
    elif n1.data<t.data and n2.data<t.data:
        findOnBst(t.left, n1, n2)
    elif t.data<n1.data and t.data<n2.data:
        findOnBst(t.right, n1, n2)
    else:
        return False

def findOneInNONBst(t,n):
    if not t:
        return None
    elif t.data==n.data:
        return True
    else:
        findOneInNONBst(t.left,n)
        findOneInNONBst(t.right,n)

def findOnNonBst(t,n1,n2):
    if t.data ==n1.data or t.data ==n2.data:
        return True
    elif findOneInNONBst(t.left, n1) and findOneInNONBst(t.right, n2):
        return False
    elif findOneInNONBst(t.left, n2) and findOneInNONBst(t.right, n1):
        return False
    else:
        findOnNonBst(t.left,n1,n2)
        findOnNonBst(t.right,n1,n2)

def findOnNonBst2(t,n1,n2, found1=False, found2=False): # and this is wrong
    # too complex, do not use even one extra param if possible, only use extra param for return results
    if not t:
        return[found1, found2]
    elif t.data == n1.data or t.data==n2.data:
        return [True,True]
        findOnNonBst2(t.left, n1, n2, True, found2)
        findOnNonBst(t.right, n1, n2, True, found2)
    elif t ==n2:
        findOnNonBst2(t.left, n1, n2, found1, True)
        findOnNonBst2(t.right, n1, n2, found1, True)
    else:
        findOnNonBst2(t.left, n1, n2, found1, found2)
        findOnNonBst2(t.right, n1, n2, found1, found2)

