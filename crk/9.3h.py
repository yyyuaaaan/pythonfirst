"""__author__ = 'anyu'

A magic index in an array A[l.. .n-l] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?,then i will use linear scan

Question 1 is slightly easier: we simplyl use binary search, and we are able to discard half of the array each time.

if (array[mid] > mid), then we discard the right half.
if (array[mid] < mid), then we discard the left half.
Question 2 is difficult. We cannot discard half of the input any more. Instead, we discard a range between (mid)
and (array[mid]). Then check left and right part seperately.


"""

def mindex2(array, l, r):
    """
    use indes l r is better
    :param array:
    :param l:
    :param r:
    :return:
    """
    if len(array)==0:
        return
    if l<0 or r>= len(array):
        return

    mid = (l+r)/2
    if array[mid] == mid:
        return mid
    elif array[mid]>mid:
        return mindex2(array, l, mid)
    else:
        return mindex2(array, mid+1, r)

