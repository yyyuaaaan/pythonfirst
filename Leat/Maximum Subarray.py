"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 int maxSubArray(int A[], int n) {
        int res = A[0];
        int dp = A[0];
        for (int i = 1; i < n; ++i) {
            dp = max(A[i], dp + A[i]);
            res = max(dp, res);
        }
        return res;
    }

"""

def maxsubarray(A,n):
    res = A[0]
    dp = A[0]
    for i in range(1,n):
        dp = max(A[i],dp+A[i-1])
        res = max(dp, res)
    return res