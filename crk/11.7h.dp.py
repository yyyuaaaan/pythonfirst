"""__author__ = 'anyu'
11.7 A circus is designing a tower routine consisting of people standing atop one another's shoulders.
For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her.
Given the heights and weights of each person in the circus, write a method to compute the largest possible number
of people in such a tower.

EXAMPLE:
Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)

this is actually:
We have a list of pairs of items. Find the longest sequence such that both the first and
second items are in non-decreasing order.
we can relate this problem to finding the longest increasing sequence in an array (LIS)
BOX STACKING

for this practical problem,assume height and weight of two people can not be the same, if it is, just "80.001",will do
then: sort one dimension of the pairs such as height, then find the longest increasing subsequence of another dimension.

 derive a recursive algorithm
 First, we need to observe that knowing the longest increasing subsequence for A[9]through A[i]
 willnot giveus the answer for A[i + l]andA[i + 2].
 However, we can use a different recursive approach. Rather than trying to find the longest increasing
 subsequence across elements 0 through i, we can find the longest subsequence which ends with element i.
 Array: 13, 14, 19, 11, 12
 Longest(ending with A[0]): 13
 Longest(ending with A[l]): 13, 14
 Longest(ending with A[2]): 10
 Longest(ending with A[3]): 10, 11
 Longest(ending with A[4]): 10, 11, 12
 Note that the longest sequence ending with A[i] can be found by looking at all the
 prior solutions.We simply append A[i] to the longest "valid"one,where valid means any list where A[i] > list.tail.
 This algorithm operates in 0(n2) time.

"""

class person(object):
    def __init__(self,h,w):
        self.h = h
        self.w = w

p0 = person(60,100)

p = [p0,p1,p2,p3]
d = [None]*len(p)

#wrong!
#t= sorted(p,key =(p.h,p.w)) # two keys or sorted(student_objects, key=attrgetter('grade', 'age'))

def lis(p,n): #n is len of p
    """
    assume p is sorted array of persons according to heights
    """
    k = 1
    d[0] = p0.w
    for i in range(1,n):
        if p[i].w >= d[k-1]:
            d[k] = p[i].w; k += 1
        else:
            for j in reversed(range(k)) and d[j]>p[i].w:
                d[j+1] = p[i].w
    return k


# correct
def LIS(arr):
    if not arr:
        return
    d=[None]*len(arr)
    res=1
    d[0]=1
    for i in range(1,len(arr)):
        d[i]=1
        for k in range(i):
            if d[k]+1>d[i] and arr[k]<=arr[i]:
                d[i]=d[k]+1
        if d[i]>res:
            res = d[i]
    return res

s=[5, 3, 4, 8, 6, 7]
print LIS(s)