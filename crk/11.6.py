"""__author__ = 'anyu'

11.6 Given an MX N matrix in which each row and each column is sorted in ascending order, write a method to find an element.

As a first approach, we can do binary search on every row to find the element. This algorithm will be 0(M log(N))
This is a good approach to mention to your interviewer before you proceed with generating a better algorithm.
"""

def search(matrix,m,n,x):
    """
    O(m+n), from upperright to downleft
    """
    r=0
    c=n-1
    while r<m and c>=0:
        if x == matrix[r][c]: return [r,c]
        if x>matrix[r][c]: r +=1
        else: c-=1
    return -1

m =[[15,20,40,85], [20,35,80,95], [30,55,95,105], [40,80,100,120]]

print search(m,4,4,20)

"""

Alternatively, we can apply a solution that more directly looks like binary search.
The code is considerably more complicated, but it applies many of the same learnings.
If you read all this code and thought, "there's no way I could do all this in an interview!" you're probably right.
You couldn't. But, your performance on any problem is evaluated compared to other candidates on the same problem.
So while you couldn't implement all this, neither can they. You are at no disadvantage when you get a tricky problem like this.
"""