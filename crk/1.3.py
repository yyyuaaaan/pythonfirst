"""

__author__ = 'anyu'

1.3 Given two strings,write a method to decide if one is a permutation of the other.
anagram
"""


def is_str_same_permu2(str1,str2): # right
    """
    using sorted() and then compare
    complexity O(nlogn)
    """
    return sorted(str1) == sorted(str2)

def is_str_same_permu2(str1,str2): # right
    """
    counting chars,
    o(n)
    using two hash table for good reason, space exchange for time.
    and good to maintain. easy to understand.
    O(n)
    """
    htable1={}
    for char in str1:
        if char not in htable1:
            htable1[char]=1  # or dic1[char] = dic1.get(char,0)+1
        else:
            htable1[char]+=1

    for char in str2:
        if char not in htable1:
            return False
        else:
            htable1[char]-=1
    for i in htable1.values():
        if i !=0:
            return False # ctci only check i<0; wrong, might be i >0
    return True





print is_str_same_permu2("fdass","fdass")

