"""__author__ = 'anyu'
Given a sorted array of n integers that has been rotated an unknown number of times,
give an O(log n) algorithm that finds an element in the array. You may assume that the array was originally
sorted in increasing order.

\
"""
def findElem(a,key,start,end):
    """
    half of the array must be ordered normally (in increasing order), and mid must be at an ordered half
    Note that while this problem is not conceptually very complex,it is actually very difficult to implement flawlessly.
    Don't feel bad if you had trouble implementing it without a few bugs. Because of the ease of making off-by-one and
    other minor errors,you should make sure to test your code very thoroughly.
    """

    #mid = (len(a)-1)//2 #,this is wrong!, because len(a) is not recursiveAvoid overflow, same as M=(L+R)/2
    mid = (start+end)//2
    if a[mid] == key: return mid
    else:
        if a[start]<=a[mid]: #the bottom half is sorted
            if a[start]<=key and key< a[mid]:
                findElem(a,key,start,mid-1)
            else:
                findElem(a,key,mid+1,end)
        else:            #the upper half is sorted
            if a[mid]<key and key<=a[end]:
                findElem(a,key,mid+1,end)
            else:
                findElem(a,key,start,mid-1)
    return None

print findElem([3, 4, 5, 1, 2,5],5,0,4) # duplicate item will fail