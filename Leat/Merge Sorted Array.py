"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
The number of elements initialized in A and B are m and n respectively.

 Solution: From back to forth.
 */

class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        int i = m - 1;
        int j = n - 1;
        int x = m + n - 1;
        while (i >= 0 && j >= 0)
            if (A[i] >= B[j]) A[x--] = A[i--];
            else A[x--] = B[j--];
        while (j >= 0) A[x--] = B[j--];
    }
};
"""
def merge(A,m,B,n):
    i = m-1
    j = n-1
    x = m+n-1
    while i>=0 and j >=0:
        if A[i]>=B[i]:
            A[x]=A[i]
            x-=1
            i-=1
        else:
            A[x]=B[j]
            x-=1
            j-=1
    while j>=0:
        A[x]=B[j]
        x-=1
        j-=1
    return A

