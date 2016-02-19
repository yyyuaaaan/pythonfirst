"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
 Do not allocate extra space for another array, you must do this in place with constant memory.
 For example,
 Given input array A = [1,1,2],
 Your function should return length = 2, and A is now [1,2].

 Solution: Update 7/16/2013: Let j start from 0 for better understanding.
 */

class Solution {
public:
    int removeDuplicates(int A[], int n) {
        int j = 0;
        for (int i = 0; i < n; ++i)
            if (i == 0 || A[i] != A[i-1])
                A[j++] = A[i];
        return j;
    }
};

"""

def remov(A,n):
    j = 0
    for i in range(n):
        if i is 0 or A[i] is not A[i-1]:
            A[j] = A[i]
            j += 1
    return j

