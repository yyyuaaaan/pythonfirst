"""__author__ = 'anyu'
9.5 Write a method to compute all permutations of a string
This solution takes 0(n !) time, since there are n! permutations. We cannot do better than this.
"""

def perm(l):
    """
    get every element in l, then recurse and perm the rest, the for the temp result add first ele to the front
    :param l: a list of chars
    :return:

    """
    if not l:
        return []
    elif len(l) ==1:
        return [l]
    else:
        result = []
        for i in range(len(l)):
            tempperm= perm(l[:i]+l[i+1:])
            [result.append([l[i]]+p) for  p in tempperm] # or result += [   l[i]]+p  for p in tempperm]

        return result
print perm([1,2,3])

for x in permuiter("abc"):print x
