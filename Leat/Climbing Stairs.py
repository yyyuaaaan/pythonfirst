"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 Solution: Clime one step from last stair or clime 2 steps from the last last stair.
 */

class Solution {
public:
    int climbStairs(int n) {
        int last = 1;
        int lastlast = 1;
        for (int i = 2; i <= n; i++)
        {
            int step = last + lastlast;
            lastlast = last;
            last = step;
        }
        return last;
    }
};
"""

def climbstairs(n):
    last = 1
    lastlast =1
    for i in range(2,n+1):
        step = last + lastlast
        lastlast = last
        last = step
    return last


def climbStairs2(n):
    if n is 1: return 1
    elif n is 2: return 2
    else:
        return climbStairs2(n-1)+climbStairs2(n-2)

def climbStairs3(n):
    dp=[None]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

print climbstairs(10)
print climbStairs2(10)
print climbStairs3(10)