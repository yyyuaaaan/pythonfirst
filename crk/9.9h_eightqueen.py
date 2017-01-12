"""__author__ = 'anyu'
8.8 Write an algorithm to print all ways of arranging eight queens on a chess board
so that none of them share the same row, column or diagonal.

Observe that since each row can only have one queen, we don't need to store our board as a full 8x8 matrix.
We only need a single array where column [row] = c indicates that row r has a queen at column c.

    search row by row, use column to store choices
    coordination starts at 0
    http://rosettacode.org/wiki/N-queens_problem#Python

an arrey of len 8 is enought, index is row, data is col result
"""

def isfree(col,queens):
    """
    test if the next col is ok to put a queen
    :param col:
    :param queens:
    :return:
    """
    if col in queens:
        return False
    elif any([ abs(col-col1)==len(queens)-index for index,col1 in enumerate(queens)]):
        #c[r]==c[j]; r-j==c[r]-c[j]; r-j==c[j]-c[r]
        # col is the colomn to check; len(queens) just be the row index of col, dont subtract 1
        return False
    else:
        return True

def solve(n):
    solutions=[[]]
    for row in range(n):
        solutions = [
            solution +[col]
            for solution in solutions # first for clause is evaluated immediately
            for col in range(n)   # so "solutions" is correctly captured
            if isfree(col, solution)
        ]
    return solutions

# if just want one solution, then solutions=iter() will do, answers.next()
answers = solve(8) # eight queens, correct, coz use range(n) and index to n-1

for answer in answers:
    print(answer)
