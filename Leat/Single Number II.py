"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


 Solution: Count the number of each bit.
*/

class Solution {
public:
    int singleNumber(int A[], int n) {
        int res = 0;
        for (int i = 0; i < 32; ++i)
        {
            int count = 0, bit = 1 << i;
            for (int j = 0; j < n; ++j)
                if (A[j] & bit)
                    count++;
            if (count % 3 != 0)
                res |= bit;
        }
        return res;
    }
};

"""
# idea: think of the final answer as the value that all bits count together
# the result should be all bits in a certain position mod 3 == 1, the
# corresponding value


def singleNumber(A):
    res=0
    for i in range(32):
        count =0
        bit = 1<<i
        for j in range(n):
            if A[j] & bit:
                count+=1
        if count%3 is not 0:
            res |=bit
    return res

A = [1, 1, 1, 3, 3, 3, 10000]
print singleNumber(A)
