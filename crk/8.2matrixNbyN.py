"""__author__ = 'anyu'
Imagine a robot sitting on the upper left hand corner of an rxc grid. The robot can only move
in two directions: right and down. How many possible paths are there for the robot?
FOLLOW UP
Imagine certain squares are "off limits", such that the robot can not step on them. Design an algorithm to
get a path for the robot.
find a path is much easier,  finds all paths is miserably complex

"""

def nways(r,c):
    """
    is it just 2^(r+c-2)?, coz r+c-2 steps in total, each step 2 options. Wrong!, permu, not btree
    set upperleft location (0,0), downright coordination(r-1,c-1)
    move from (r-1,c-1) to (0,0)

    if multiple "off limits",just turn x0 and y0 into two array
    input r rows, c cols, r*c nodes
    to make such clear, draw and write on paper is much simple
    """
    if r<0 or c<0:
        return 0
    elif r==1 or c==1:
        return 1
    else:
        return nways(r-1,c) + nways(r,c-1)
print nways(3,3)

def getallpath(r,c,onepath=[]):
    if r==0 and c ==0:
        print onepath
        return # can't return paths or paths[i], can't yield paths, coz gonna recurse
    else:
        if r>0:
            getallpath(r-1,c,onepath+[(r-1,c)] )
        if c>0:
            getallpath(r,c-1,onepath+[(r,c-1)] )
print getallpath(2,2)

def findOnePathswithOffs(M ,r=len(M),c=len(M[0]),path=[]): # with off nodes
    """
    matrix input with off nodes to avoid with True or False
    wrong representation:  def nways(r,c, offx=2,offy=1):
    exponential time
    """
    if c<0 or r<0 or not M[r,c]:
        return False
    else:
        if c==0 and r==0 \
                or findOnePathswithOffs(M, r-1,c,path)\
                or findOnePathswithOffs(M, r,c-1,path):
            path.append((r,c))
            return True
    return False

def getapath(x,y,path=[],offxy=[]):    # with off nodes
    """
    only find one path, use backtracking from x,y to 0,0
    when get to 0,0, stack just have one path
    backwards from x,y to 0,0
    try and err
    """
    path.append([x,y])
    suc = False
    if x is 0 and y is 0:
        suc = True
        print path
    elif x>0 and (x-1,y) not in offxy and getapath(x-1,y,path):
        path.append((x-1,y))
    elif y>0 and (x,y-1) not in offxy and getapath(x,y-1,path):
        path.append((x,y-1))
    else:
        path.pop()
    return suc # if return suc is true, then path will store a right pass.

print getapath(2,2)
