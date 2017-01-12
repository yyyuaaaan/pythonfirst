"""

__author__ = 'anyu'

Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0
"""

def set_ma_zero(ma,M,N):
    tempset=set()   # void set can not be tempset={}, that is dict
    for m in range(M):
        for n in range(N):
            if ma[m][n] == 0:
                tempset.add((m,n)) # list can not be hashable, so [m,n] is not ok.

    print tempset
    for [x,y] in tempset:
        ma[x]=[0]*N
        for i in range(M):
            ma[i][y]=0

    return ma

print  set_ma_zero([[1,2,3],[4,5,5],[7,8,9],[22,11,12]],4,3)
print  set_ma_zero([[1,2,3],[4,5,0],[7,8,9],[0,11,12]],4,3)
