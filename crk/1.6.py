def rotatematrix(m):
    """
    __author__ = 'anyu'

Given an image represented by an NxN matrix, where each pixel in
 the image is 4 bytes, write a method to rotate the image by 90 degrees.
 Can you do this in place?
0(N2)

#diagonal mirror
    for i in range(len(m)):
        for j in range(i):
            m[i][j],m[j][i] = m[j][i],m[i][j]

    transpose
    return [[row[i] for row in m] for i in range(len(m))]

    transpose
    zip(*dia) *operator to unzip


# anti-diagonal mirror
for i in xrange(n):
for j in xrange(n - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

# horizontal mirror
for i in xrange(n / 2):
for j in xrange(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3
    """
    # first do horizontal mirror
    mid=len(m)/2
    for i in range(mid):
        m[i],m[len(m)-1-i] = m[len(m)-1-i],m[i]

    # then zip/transpose
    return zip(*m)


dia=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print rotatematrix(dia)
print [[row[i] for row in dia] for i in range(len(dia))]


