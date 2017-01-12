"""__author__ = 'anyu'
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move
in two directions: right and down. How many possible paths are there for the robot?
FOLLOW UP
Imagine certain squares are "off limits", such that the robot can not step on them. Design an algorithm to
get a path for the robot.
find a path is much easier,  finds all paths is miserably complex

"""

def nways(n,x=0,y=0):
    """
    x,y,<n
    set upperleft location (0,0), downright coordination(n,n)
    if multiple "off limits",just turn x0 and y0 into two array
    :param n:
    :param x:
    :param y:
    :return:
    """
    if x ==n and y ==n:
        return 1
    elif x >=n:
        return 1
    elif y >=n:
        return 1
    else:
        return nways(n,x+1,y)+nways(n,x,y+1)

print nways(3,0,0)

def isfree(x,y):
    if [x,y] in [[2,1],[1,2]]:return False
    else:return True

def getapath(x,y,path=[]):
    """
    only find one path, use backtracking from x,y to 0,0
    when get to 0,0, stack just have one path
    backwards from x,y to 0,0
    """
    path.append([x,y]) # path as an stack, try and error
    suc = False
    if x is 0 and y is 0:
        suc = True
        print path
    elif x>=1 :  # and isfree(x,y) if no isfree function then, we can still find a path
        suc = getapath(x-1,y,path)
    elif suc is False and y>=1: # and isfree(x,y)
        suc = getapath(x,y-1,path)
    elif suc is False:
        path.pop()
    return suc # if return suc is true, then path will store a right pass.

def getallpath(m,n,M,N,path=[]):
    """
    move backwards from m,n to 0,0
    :param m:
    :param n:
    :param path:
    :return:
    """
    if m>M:
        path.pop()
        return
    if n>N:
        path.pop() # path as a stack
        return

    # if isfree(m,n) is False: path.pop()  simple to exclude other spots

    if m ==M and n ==N:
        print path
        # no need, because returned and path not preserved for another path
        #while path: #    path =[] not gonna work, can't transfer back to recursion
        #    path.pop()  # also this is wrong, coz pop too early? hard
        return
    else:
        getallpath(m+1,n,M,N,path+[[m+1,n]])
        getallpath(m,n+1,M,N,path+[[m,n+1]])


#both is correct
def getallpath(m,n,M,N,path=[]):
    """
    move backwards from m,n to 0,0
    :param m:
    :param n:
    :param path:
    :return:
    """
    # if isfree(m,n) is False: path.pop()  simple to exclude other spots

    if m ==M and n ==N:
        print path
        # no need, because returned and path not preserved for another path
        #while path: #    path =[] not gonna work, can't transfer back to recursion
        #    path.pop()  # also this is wrong, coz pop too early? hard
        return
    else:
        if m<M:
            getallpath(m+1,n,M,N,path+[[m+1,n]])
        if n<N:
            getallpath(m,n+1,M,N,path+[[m,n+1]])

getallpath(0,0,3,3)

getallpath(0,0,3,3)