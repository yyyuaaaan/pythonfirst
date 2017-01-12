"""__author__ = 'anyu'

Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent),
write code to calculate the number of ways of representing n cents.


This question is as same as "combination sum" in leetcode.
the solution of that question is more general and easy to remember.

"""

# leetcode version is more intuitive

""" wrong! the combination is in order, but THE problem solution do not have order, too many repetition
def f(n):
    if n < 0: return 0
    if n in range(0,5):return 1
    if n in range(5,10):return f(n-1)+f(n-5)
    if n in range(10,25):return f(n-1)+f(n-5)+f(n-10)
    if n >=25: return f(n-1)+f(n-5)+f(n-10)+f(n-25)

print f(30)
"""

def f(n):
    """
    first use 25 cents, then use 10 cents... use big denom first, then (10,5) and (5,10) will not be recounted
    because after you use up 10 cent coin, you will not use 10 cent any more.


    """
    count = 0
    for i in range(n//25+1):
        for j in range(n//10+1):
            for k in range(n//5+1):
                for l in range(n+1):
                    v = i * 25 + j * 10 + k * 5 + l
                    if v ==n: count+=1
                    elif v>n: break   # this line will gain some efficiency, because for loop execute iteratively
    return count


print f(100)
