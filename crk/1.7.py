"""

__author__ = 'anyu'

Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0
"""

def set_ma_zero(ma,M,N):
    row=set()
    col=set() # set element must be hashable, list not ok
    for i in range(M):
        for j in range(N):
            if ma[i][j]==0:
                row.add(i)
                col.add(j) # if already in set, can still add j, no repetitions

    for ele in row:
        for j in range(N):
            ma[ele][j]=0

    for ele2 in col:
        for i in range(M):
            ma[i][ele2]=0
    return ma

print  set_ma_zero([[1,2,3],[4,5,5],[7,8,9],[22,11,12]],4,3)
print  set_ma_zero([[1,2,3],[4,5,0],[7,8,9],[0,11,12]],4,3)
