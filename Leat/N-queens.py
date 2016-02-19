"""
// solution 1: recursion
    int totalNQueens_1(int n)
    {
        int board[n];
        memset(board, -1, sizeof(board));
        int res = 0;
        totalNQueensRe(n, 0, board, res);
        return res;
    }

    void totalNQueensRe(int n, int row, int board[], int &res)
    {
        if (row  == n)
        {
            res++;
            return;
        }
        for (int i = 0; i < n; ++i)
        {
            if (isValid(board, row, i))
            {
                board[row] = i;
                totalNQueensRe(n, row + 1, board, res);
                board[row] = -1;
            }
        }
    }

    bool isValid(int board[], int row, int col)
    {
        for (int i = 0; i < row; ++i)
            if (board[i] == col || row - i == abs(col - board[i]))
                return false;
        return true;
    }
"""