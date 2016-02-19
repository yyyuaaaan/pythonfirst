"""__author__ = 'anyu'
9.1 A child is running up a staircase with n steps, and can hop either 1step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""

def npermu(n):
    if n ==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return npermu(n-1)+npermu(n-2)+npermu(n-3)

print(npermu(10))

def count_ways_iter_haha(n):
    """
    iteratively, do not even maintain a array, only 6 temp variables
    """
    if n <0: return 0
    if n is 0: return 1
    if n is 1: return 1

    t1=0; t2=1; t3=1

    for i in range(2,n+1):
        t4= t1+t2+t3
        t1=t2
        t2=t3
        t3=t4
    return t4

print count_ways_iter_haha(10)