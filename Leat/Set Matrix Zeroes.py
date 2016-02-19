"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

 Solution: Use first row and column as auxiliary spaces instead of newly allocating ones.
 (no need; hard to comprehand)





"""
def setzeromatrix(matrix=[[]]):
    res =[]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] ==0:
                res += [i,j]

    for m in [x[0] for x in res]:
        # set row zero
        pass
    for n in [x[1] for x in res]:
        # set col zero
        pass

