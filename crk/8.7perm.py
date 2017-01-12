"""__author__ = 'anyu'
8.7 8.8 Write a method to compute all permutations of a string
with or without duplicates?

with dups, use hashtable to maintain res, slow!; use counts of chars dict to maintain counts, build perm from groundup
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

def powerset(s=[]):
    if not s:
        return [[]]
    else:
        return powerset(s[:-1])      +    [subset+[s[-1]]  for subset in powerset(s[:-1])]

def perm(l=[]):

    if not l:
        return
    if len(l)==1:
        return [l]
    else:
        t =[[]]
        for oneperm in perm(l[1:]):
            for i in range(len(oneperm)):
                t+= oneperm[:i] +[l[0]] +oneperm[i:]
        return t

print perm([1,2,3])


for x in perm([1,2,3]):print x
