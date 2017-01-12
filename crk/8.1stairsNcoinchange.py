"""__author__ = 'anyu'
9.1 A child is running up a staircase with n steps, and can hop either 1step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.

not permutation and not combination
"""

def npermu(n):
    if n<=0: return 0
    elif n ==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return npermu(n-1)+npermu(n-2)+npermu(n-3)

def npermuiter(n):
    if n<0: return 0
    elif n==0:
        return 1
    elif n ==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        t1=1
        t2=2
        t3=4
        for i in range(4,n+1):
            temp= t1+t2+t3
            t1=t2
            t2=t3
            t3=temp
        return temp

print npermuiter(10)

coins = [1, 2, 5]
amount = 11

def minNumOfCoin(amount, coins):
    """
    for j in range (amountsum)
       for valuei in [coins]
       m(j) = min(m(j-valuei))+1
    M(i) = min(M(i-1), M(i-2),M(i-5))+1

    wrong thinking: l to hold t1 t2 t5, coz we may also need t4
    wrong thinking: recursion,
    right thinking: creat an array where index is just range(amount),
    right thinking: forward dp
    """

    maxnum=10000
    res=[maxnum]*(amount+1)
    for x in coins:
        if x <amount+1:
            res[coins] =1

    for i in range(1,amount+1):
        for denom in coins:
            if i-denom>0 and res[i-denom] is not maxnum:
                res[i] = min(res[i-denom]+1, res[i])

    return res[-1] if res[-1] is not maxnum else -1
