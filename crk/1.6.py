
"""

__author__ = 'anyu'

Given an image represented by an NxN matrix, where each pixel in
 the image is 4 bytes, write a method to rotate the image by 90 degrees.
 Can you do this in place?
0(N2)
"""

def matrixro(ma):
    N= len(ma)
    ma = zip(*ma) # transpose matrix, very interesting, aij = aji,
    #ther ways to transpose
    [[row[i] for row in matrix] for i in range(4)]

    #for i in range(4):
    #    for j in range(i,4):
    #       dia[i][j],dia[j][i]=dia[j][i],dia[i][j]

    N2= N//2
    for k in range(N2):
        ma[k],ma[N-1-k] = ma[N-1-k], ma[k] # swap row[k] and row[N-1-k]
    return ma


dia=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]

print matrixro(dia)

