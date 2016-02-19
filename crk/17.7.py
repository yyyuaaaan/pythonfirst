"""__author__ = 'anyu'
19.7 You are given an array of integers (both positive and negative).
Find the continuous sequence with the largest sum. Return the sum.
a = [2, -8, 3, -2, 4, -10]
d[0]=0
d[i]=Max[ d[i-1]+a[i], a[i] ] # current big sum ends with a[i]
max[d] =

output: sum[3, -2, 4]
"""

def maxsum(a):

    d = [None]*(len(a))
    d[0] = 2
    for i in range(1,len(a)):
        if d[i-1]+a[i] > a[i]:
            d[i]=d[i-1]+a[i]
        else:
            d[i]=a[i]
    return max(d)

a = [2, -8, 3, -2, 4, -10]

print maxsum(a)