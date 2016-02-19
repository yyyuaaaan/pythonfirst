"""
newton method

f(x) = f(xi) + f`(xi)(x - xi)
xi+1=xi - f(xi) / f`(xi)

xi+1=xi - (xi2 - n) / (2xi) = xi - xi / 2 + n / (2xi) = xi / 2 + n / 2xi = (xi + n/xi) / 2
"""

def sqt(x):

    epsilon = 0.001

    if abs(x-0)<epsilon: return 0
    last = float(0)
    res = float(1)

    while abs(res - last)>=epsilon:
        last = res
        res = (res + x/res)*0.5
    return res

print sqt(1)

