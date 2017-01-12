
"""

__author__ = 'anyu'

Implement a function void reverse (char* str) in C or C++
which reverses a null-terminated string.
Just reverse a string.
"""

# if we recursively do this problem, it will take too much space, not in place,
# because everytime the python interpreter calls a recursive function, it set
# a new stack frame, it is too costly, in other languges surporting CPS transformation
# we can use recursive way.

def reverse(s):
    if not s:
        return s
    return reverse(s[1:])+s[0]

def reversestr(s):
    """

    :param s: input string
    :return:  reversed string
    """
    if not s or len(s) ==1:
        return s
    else:
        return ''.join(s[-1]+reversestr(s[1:-1])+s[0])

print reversestr('fsasdf')

def reverse2(s):
    if not s:
        return s
    if len(s)==1:
        return s
    else:
        l = list(s)
        for i in range(len(s)/2):
            # switch two chars
            l[i], l[len(s)-i-1] = l[len(s)-i-1], l[i]
        return ''.join(l)

print reverse2("asdf")
