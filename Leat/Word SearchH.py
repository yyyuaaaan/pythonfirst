"""__author__ = 'anyu'
Given a 2D board and a word, find if the word exists in the grid.
 The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
 those horizontally or vertically neighboring. The same letter cell may not be used more than once.
 For example,
 Given board =
 [
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
 ]
 word = "ABCCED", -> returns true,
 word = "SEE", -> returns true,
 word = "ABCB", -> returns false.

 Solution: DFS. (For 'visited', using two-dimensional array will be faster than vector<vector>.[90+ms->50+ms])
"""
def wordSearch(matrix, w):
    '''
    search for words in matrix
    '''
    def _search(x, y, depth, w):
        '''
        dfs,backtrack
        '''
        if depth == len(w):
            result[0] = True
            return
        if result[0] or x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return

        if matrix[x][y] == w[depth]:
            temp = matrix[x][y]
            matrix[x][y] = -1 # visited
            _search(x - 1, y, depth + 1, w)
            _search(x + 1, y, depth + 1, w)
            _search(x, y + 1, depth + 1, w)
            _search(x, y - 1, depth + 1, w)
            matrix[x][y] = temp

    result = [False]    # result = False is not ok, need to be a list to be reference by _search
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            _search(i, j, 0, w)
            if result[0]:
                return True
    return False


if __name__ == '__main__':
    matrix = [
        list("ABCE"),
        list("SFCS"),
        list("ADEE")
    ]
    words = ['SEE', 'ABCB', 'ABCCED']

    for w in words:
        print(wordSearch(matrix, w))