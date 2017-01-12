# Recursive Multiply: Write a recursive function to multiply two positive integers without using the *operator.
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

def mulitiply(x,y):
    """
    positive num
    :param x:
    :param y:
    :return:
    """
    if x==0 or y==0:
        return 0
    x, y = min(x,y),max(x,y)

    return m(x,y)

def m(x,y):
    if x ==0:
        return 0
    elif x%2 is 0: #last bit is 0 or 1
        return m(x>>1,y)+m(x>>1,y)
    else:
        return m(x>>1,y)+m(x>>1,y) +y

print mulitiply(3,4)
