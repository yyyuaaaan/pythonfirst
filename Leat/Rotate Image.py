"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

 Solution: 1. 123   ->  147   ->   741    (preferable)
              456       258        852
              789       369        963
 void rotate_2(vector<vector<int> > &matrix) {
        int N = matrix.size();
        for (int i = 0; i < N; ++i)
            for (int j = i+1; j < N; ++j)
                swap(matrix[i][j], matrix[j][i]);
        for (int j = 0; j < N/2; ++j)
            for (int i = 0; i < N; ++i)
                swap(matrix[i][j], matrix[i][N-j-1]);
    }
"""
def rotate(matrix):
    n = len(matrix)   # j row, i col
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

    for j in range(n/2):
        for i in range(n):
            matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1],matrix[i][j]