"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int i = 0;
        for (int j = 0; j < n; ++j)
            if (A[j] != elem)
                A[i++] = A[j];
        return i;
    }
};
"""
def removelement(A,e):
    j=0

    for i in range(len(A)) :
        if A[i] == e:
            continue
        else:
            A[j] = A[i]
            j+=1
    return j
