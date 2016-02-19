"""
9.6 Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n-pairs of parentheses.
EXAMPLE:
input: 3 (e.g., 3 pairs of parentheses)
output: ((())), (()()), (())(), ()(()), ()()()

(, left = 1, right = 0
((, left = 2, right = 0
((), left = 2, right = 1
(()(, left = 3, right = 1
(()(), left = 3, right = 2
(()()), left = 3, right = 3

1. Left Paren: As long as we haven't used up all the left parentheses, we can always
insert a left paren.
2. Right Paren: We can insert a right paren as long as there are less right parentheses than left.

Because we insert left and right parentheses at each index in the string,
and we never repeat an index, each string is guaranteed to be unique.

"""

def paren(npairs,left=0,right=0,stringout=[]):

    if left == npairs and right == npairs:
        print stringout
        return
    else:
        if left<npairs:
            paren(npairs,left+1,right,stringout+["("])

        if right<left:
            paren(npairs,left,right+1,stringout+[")"])

paren(3)

