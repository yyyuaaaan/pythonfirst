"""
Given an array of integers, every element appears twice except for one.
 Find that single one.
 Your algorithm should have a linear runtime complexity.
 Could you implement it without using extra memory?

 Solution: XOR.
*/

class Solution {
public:
    int singleNumber(int A[], int n) {
        for (int i = 1; i < n; ++i)
            A[0] ^= A[i];
        return A[0];
    }
};

"""
def singleNumber(A,n):
    for i in range(1,len(A)-1):
        A[0] ^=A[i]
    return A[0]

import operator
def singleNumber2(A):
    return reduce(operator.xor, A)
