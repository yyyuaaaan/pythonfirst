"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 Note: You can only move either down or right at any point in time.

// DP, O(m*n) time, O(m*n) space
 */

    int minPathSum1(vector<vector<int> > &grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int M = grid.size(), N = grid[0].size();
        vector<vector<int> > dp(M, vector<int>(N, 0));
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (i == 0 && j == 0) dp[i][j] = grid[i][j];
                else if (i == 0) dp[i][j] = dp[i][j - 1] + grid[i][j];
                else if (j == 0) dp[i][j] = dp[i - 1][j] + grid[i][j];
                else dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }
        return dp[M - 1][N - 1];

"""

def minpathsum(matrix):
    """
    recursion is not ok, use dp instead
    """
    m = len(matrix)
    n = len(matrix[0])

    if m <=0 or n <=0: return
    if m ==1: return sum(matrix[0])
    if n ==1: return sum([x for [x] in matrix])

    else:
        for i in range(m):
            for j in range(n):
                s = min(minpathsum(matrix))
        return minpathsum