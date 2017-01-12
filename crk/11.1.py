"""__author__ = 'anyu'
11.1 You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.

easy and tricky
"""

"""# wrong
def arraymerge(a,b,lena,lenb):
    for i in reversed(range(lena + lenb-1)):
        if b[i]> a[lena-1-i]: # here is wrong b[i] is out of range
            a[lena+lenb-1-i] = b[i]
        if b[i]<= a[lena-1-i]:
            a[lena+lenb-1-i] = a[lena-1-i]
    return a
"""



# wrong at first, sometimes, naming extravagantly is not a good thing


def merge(a,b,m,n):
    k = m+n-1
    i = m -1 # array a
    j = n -1 # array b

    while i>=0 and j>=0:
        if a[i] > b[j]:
            a[k] = a[i]
            k -= 1
            i -= 1
        else:
            a[k] = b[j]
            k -= 1
            j -= 1
    while j>=0:    # if there are still some parts of b,
        a[k] = b[j]
        k -= 1
        j -= 1
    return a



a = [1, 3, 7, 8, 9, 0, 0, 0, 0, 0]
b = [2, 4, 5, 6, 10]

print merge(a,b,5,5)

print arraymerge2(a,b,5,5)

print arraymerge(a,b,5,5)